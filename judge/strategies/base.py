# judge/strategies/base.py
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

from ..utils.path_validator import (
    validate_source_file,
    validate_work_dir,
    validate_file_path,
    PathValidationError,
)
from ..utils.resource_limiter import (
    ResourceLimits,
    ResourceMonitor,
    MemoryLimitExceeded,
    TimeLimitExceeded,
    OutputLimitExceeded,
    ExecutionResult,
    OutputLimitChecker,
    resource_limit_context,
    get_resource_stats,
    DEFAULT_LIMITS,
)


class BaseJudgeClient(ABC):
    """判题客户端基类"""

    def __init__(self) -> None:
        super().__init__()
        self._resource_limits: Optional[ResourceLimits] = None
    
    @property
    def default_resource_limits(self) -> ResourceLimits:
        """
        返回默认资源限制
        子类可重写此方法以提供不同的默认值
        """
        return DEFAULT_LIMITS
    
    def set_resource_limits(
        self,
        memory_mb: Optional[float] = None,
        time_ms: Optional[float] = None,
        stack_mb: Optional[float] = None,
        cpu_time_ms: Optional[float] = None,
        memory_buffer_mb: Optional[float] = None,
        output_limit_kb: Optional[float] = None,
    ) -> None:
        """
        设置资源限制
        
        Args:
            memory_mb: 内存限制 (MB)
            time_ms: 时间限制 (毫秒)
            stack_mb: 栈大小限制 (MB)
            cpu_time_ms: CPU时间限制 (毫秒)
            memory_buffer_mb: 内存冗余 (MB)
            output_limit_kb: 输出限制 (KB)
        """
        current = self._resource_limits or self.default_resource_limits
        
        self._resource_limits = ResourceLimits(
            memory_mb=memory_mb if memory_mb is not None else current.memory_mb,
            time_ms=time_ms if time_ms is not None else current.time_ms,
            stack_mb=stack_mb if stack_mb is not None else current.stack_mb,
            cpu_time_ms=cpu_time_ms if cpu_time_ms is not None else current.cpu_time_ms,
            memory_buffer_mb=memory_buffer_mb if memory_buffer_mb is not None else current.memory_buffer_mb,
            output_limit_kb=output_limit_kb if output_limit_kb is not None else current.output_limit_kb,
        )
    
    def get_resource_limits(self) -> ResourceLimits:
        """获取当前资源限制"""
        return self._resource_limits or self.default_resource_limits
    
    def _validate_exec_file(self, exec_file: str, work_dir: str) -> str:
        """验证执行文件路径"""
        return validate_file_path(exec_file, work_dir)

    def _validate_source_file(self, source_file: str) -> str:
        """验证源文件路径"""
        return validate_source_file(source_file)

    def _validate_work_dir(self, work_dir: str) -> str:
        """验证工作目录路径"""
        return validate_work_dir(work_dir)

    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        """
        返回执行命令
        exec_command() -> ['python3', source]
        """

    @property
    @abstractmethod
    def extension_name(self) -> str:
        """
        返回扩展名名称
        """

    @property
    @abstractmethod
    def language_name(self) -> str:
        """
        返回语言名称
        """

    @abstractmethod
    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回编译命令
        comp_command() -> ['gcc', source, '-o', source]
        """
    
    def execute_with_limits(
        self,
        exec_file: str,
        work_dir: str,
        stdin_data: Optional[str] = None,
        output_limit_kb: Optional[float] = None,
    ) -> ExecutionResult:
        """
        执行命令并应用资源限制
        
        时间限制规则：
        - 在时间限制内完成：正常返回
        - 在100%-150%之间完成：判定TLE，返回实际时间
        - 超过150%：强制终止，返回150%时间
        
        内存限制规则：
        - 默认多8MB冗余
        - 使用峰值内存判定
        
        输出限制规则：
        - 默认64KB
        - SPJ可自定义
        
        Args:
            exec_file: 可执行文件路径
            work_dir: 工作目录
            stdin_data: 标准输入数据
            output_limit_kb: 输出限制 (KB)，None使用默认值
            
        Returns:
            ExecutionResult 执行结果
        """
        import subprocess
        
        limits = self.get_resource_limits()
        command = self.exec_command(exec_file, work_dir)
        
        # 输出限制检查器
        output_limit = output_limit_kb if output_limit_kb is not None else limits.output_limit_kb
        output_checker = OutputLimitChecker(limit_kb=output_limit)
        
        result = ExecutionResult(
            time_limit_ms=limits.time_ms,
            memory_limit_mb=limits.memory_mb,
            output_limit_kb=output_limit,
        )
        
        with resource_limit_context(limits) as monitor:
            try:
                proc = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE if stdin_data else None,
                    cwd=work_dir,
                    text=True,
                    bufsize=0,  # 无缓冲，实时读取
                )
                
                stdout_chunks = []
                stderr_chunks = []
                
                # 实时读取输出，检查大小
                while proc.poll() is None:
                    # 读取stdout
                    if proc.stdout:
                        chunk = proc.stdout.read(4096)
                        if chunk:
                            stdout_chunks.append(chunk)
                            if output_checker.write(chunk):
                                # 输出超限，强制终止
                                proc.kill()
                                proc.wait()
                                resource_stats = monitor.stop()
                                result.stdout = ''.join(stdout_chunks)
                                result.stderr = ''.join(stderr_chunks)
                                result.output_size_bytes = output_checker.total_bytes
                                result.ole = True
                                result.returncode = -3
                                return result
                    
                    # 短暂休眠避免CPU占用
                    time.sleep(0.001)
                
                # 获取最终输出
                stdout, stderr = proc.communicate()
                if stdout:
                    stdout_chunks.append(stdout)
                if stderr:
                    stderr_chunks.append(stderr)
                
                resource_stats = monitor.stop()
                
                result.stdout = ''.join(stdout_chunks)
                result.stderr = ''.join(stderr_chunks)
                result.returncode = proc.returncode
                result.elapsed_time_ms = resource_stats['elapsed_time_ms']
                result.peak_memory_mb = resource_stats['peak_memory_mb']
                result.output_size_bytes = output_checker.total_bytes
                
                # 判断TLE
                if resource_stats['tle']:
                    result.tle = True
                
                # 判断MLE
                if resource_stats['mle']:
                    result.mle = True
                
                # 判断OLE
                if output_checker.is_over_limit():
                    result.ole = True
                
                # 判断RE
                if proc.returncode != 0 and not result.tle and not result.mle:
                    result.re = True
                
                return result
                
            except subprocess.TimeoutExpired:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = 'Time Limit Exceeded'
                result.returncode = -1
                result.elapsed_time_ms = resource_stats['elapsed_time_ms']
                result.tle = True
                return result
            except MemoryLimitExceeded as e:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = str(e)
                result.returncode = -2
                result.peak_memory_mb = resource_stats['peak_memory_mb']
                result.mle = True
                return result
            except Exception as e:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = str(e)
                result.returncode = -99
                result.re = True
                return result


class SpecialJudgeClient(BaseJudgeClient):
    """
    Special Judge 判题客户端基类
    用于答案不唯一或需要特殊验证的题目
    """

    def _validate_judge_file(self, judge_file: str) -> str:
        """验证Special Judge文件路径"""
        return validate_source_file(judge_file)

    def _validate_input_file(self, input_file: str) -> str:
        """验证输入文件路径"""
        return validate_file_path(input_file)

    def _validate_output_file(self, output_file: str) -> str:
        """验证输出文件路径"""
        return validate_file_path(output_file)

    @abstractmethod
    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        """
        返回 Special Judge 执行命令

        Args:
            judge_file: Special Judge 程序文件路径
            input_file: 题目输入文件路径
            output_file: 用户程序输出文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表
            例如: ['./spj', 'input.txt', 'output.txt']
        """

    @abstractmethod
    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回 Special Judge 程序编译命令

        Args:
            judge_file: Special Judge 源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None
            例如: ['g++', 'spj.cpp', '-o', 'spj']
        """

    @property
    def judge_extension(self) -> str:
        """
        返回 Special Judge 程序的扩展名
        默认与主程序相同
        """
        return self.extension_name
    
    def execute_judge_with_limits(
        self,
        judge_file: str,
        input_file: str,
        output_file: str,
        work_dir: str,
        output_limit_kb: Optional[float] = None,
    ) -> ExecutionResult:
        """
        执行Special Judge并应用资源限制
        
        Args:
            judge_file: Special Judge程序路径
            input_file: 输入文件路径
            output_file: 用户输出文件路径
            work_dir: 工作目录
            output_limit_kb: 输出限制 (KB)
        """
        import subprocess
        
        limits = self.get_resource_limits()
        command = self.judge_command(judge_file, input_file, output_file, work_dir)
        
        output_limit = output_limit_kb if output_limit_kb is not None else limits.output_limit_kb
        output_checker = OutputLimitChecker(limit_kb=output_limit)
        
        result = ExecutionResult(
            time_limit_ms=limits.time_ms,
            memory_limit_mb=limits.memory_mb,
            output_limit_kb=output_limit,
        )
        
        with resource_limit_context(limits) as monitor:
            try:
                proc = subprocess.Popen(
                    command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=work_dir,
                    text=True,
                    bufsize=0,
                )
                
                stdout_chunks = []
                stderr_chunks = []
                
                while proc.poll() is None:
                    if proc.stdout:
                        chunk = proc.stdout.read(4096)
                        if chunk:
                            stdout_chunks.append(chunk)
                            if output_checker.write(chunk):
                                proc.kill()
                                proc.wait()
                                resource_stats = monitor.stop()
                                result.stdout = ''.join(stdout_chunks)
                                result.stderr = ''.join(stderr_chunks)
                                result.output_size_bytes = output_checker.total_bytes
                                result.ole = True
                                result.returncode = -3
                                return result
                    
                    time.sleep(0.001)
                
                stdout, stderr = proc.communicate()
                if stdout:
                    stdout_chunks.append(stdout)
                if stderr:
                    stderr_chunks.append(stderr)
                
                resource_stats = monitor.stop()
                
                result.stdout = ''.join(stdout_chunks)
                result.stderr = ''.join(stderr_chunks)
                result.returncode = proc.returncode
                result.elapsed_time_ms = resource_stats['elapsed_time_ms']
                result.peak_memory_mb = resource_stats['peak_memory_mb']
                result.output_size_bytes = output_checker.total_bytes
                
                if resource_stats['tle']:
                    result.tle = True
                if resource_stats['mle']:
                    result.mle = True
                if output_checker.is_over_limit():
                    result.ole = True
                if proc.returncode != 0 and not result.tle and not result.mle:
                    result.re = True
                
                return result
                
            except subprocess.TimeoutExpired:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = 'Time Limit Exceeded'
                result.returncode = -1
                result.elapsed_time_ms = resource_stats['elapsed_time_ms']
                result.tle = True
                return result
            except MemoryLimitExceeded as e:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = str(e)
                result.returncode = -2
                result.peak_memory_mb = resource_stats['peak_memory_mb']
                result.mle = True
                return result
            except Exception as e:
                resource_stats = monitor.stop()
                result.stdout = ''
                result.stderr = str(e)
                result.returncode = -99
                result.re = True
                return result


class InteractiveJudgeClient(BaseJudgeClient):
    """
    交互题判题客户端基类
    用于需要与评测程序进行交互的题目
    """

    def _validate_interact_file(self, interact_file: str) -> str:
        """验证交互评测程序文件路径"""
        return validate_source_file(interact_file)

    @abstractmethod
    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        """
        返回交互题执行命令

        Args:
            exec_file: 用户程序可执行文件路径
            interact_file: 交互评测程序文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表
        """

    @abstractmethod
    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        """
        返回交互评测程序编译命令

        Args:
            interact_file: 交互评测程序源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None
        """

    @property
    def interact_extension(self) -> str:
        """
        返回交互评测程序的扩展名
        默认与主程序相同
        """
        return self.extension_name

    @property
    def default_timeout(self) -> int:
        """
        返回默认超时时间（秒）
        交互题通常需要更长的超时时间
        """
        return 10
    
    @property
    def default_resource_limits(self) -> ResourceLimits:
        """
        交互题默认资源限制 (更长的时间限制)
        """
        return ResourceLimits(
            memory_mb=256.0,
            time_ms=10000.0,  # 10秒
            stack_mb=64.0,
            cpu_time_ms=10000.0,
            memory_buffer_mb=8.0,
            output_limit_kb=64.0,
        )
