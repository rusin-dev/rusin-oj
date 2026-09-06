# judge/utils/resource_limiter.py
"""
资源限制模块 - 精确控制内存和时间限制

时间限制规则：
- 程序在时间限制内完成：正常返回 (AC/TLE等)
- 程序在时间限制的100%-150%之间完成：判定TLE，但返回实际运行时间
- 程序超过150%时间限制：强制终止，返回150%时间
- 例：时间限制1000ms，最多运行到1500ms

内存限制规则：
- 默认多8MB冗余（避免临界情况误判）
- 使用峰值内存判定

输出限制规则：
- 默认限制64KB
- SPJ可自定义限制
"""
import os
import sys
import signal
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Tuple
from contextlib import contextmanager
from functools import wraps
import time
import threading

# 条件导入 resource 模块 (仅 Unix/Linux)
if sys.platform != 'win32':
    import resource
else:
    resource = None


class ResourceLimitError(Exception):
    """资源限制错误"""
    pass


class MemoryLimitExceeded(ResourceLimitError):
    """内存超限错误 (MLE)"""
    pass


class TimeLimitExceeded(ResourceLimitError):
    """时间超限错误 (TLE)"""
    pass


class OutputLimitExceeded(ResourceLimitError):
    """输出超限错误 (OLE)"""
    pass


@dataclass
class ResourceLimits:
    """资源限制配置"""
    memory_mb: float = 256.0      # 内存限制 (MB)
    time_ms: float = 1000.0       # 时间限制 (毫秒)
    stack_mb: float = 64.0        # 栈大小限制 (MB)
    cpu_time_ms: float = 1000.0   # CPU时间限制 (毫秒)
    memory_buffer_mb: float = 8.0 # 内存冗余 (MB)，避免临界误判
    output_limit_kb: float = 64.0 # 输出限制 (KB)，默认64KB
    
    @property
    def memory_bytes(self) -> int:
        """内存限制转换为字节 (不含冗余)"""
        return int(self.memory_mb * 1024 * 1024)
    
    @property
    def memory_bytes_with_buffer(self) -> int:
        """内存限制转换为字节 (含冗余)"""
        return int((self.memory_mb + self.memory_buffer_mb) * 1024 * 1024)
    
    @property
    def time_seconds(self) -> float:
        """时间限制转换为秒"""
        return self.time_ms / 1000.0
    
    @property
    def time_buffer_ms(self) -> float:
        """时间冗余: min(测试点的50%, 200ms)"""
        return min(self.time_ms * 0.5, 200.0)
    
    @property
    def max_time_ms(self) -> float:
        """最大允许运行时间 (含冗余) = 时间限制 + min(50%, 200ms)"""
        return self.time_ms + self.time_buffer_ms
    
    @property
    def max_time_seconds(self) -> float:
        """最大允许运行时间转换为秒"""
        return self.max_time_ms / 1000.0
    
    @property
    def stack_bytes(self) -> int:
        """栈大小转换为字节"""
        return int(self.stack_mb * 1024 * 1024)
    
    @property
    def cpu_time_seconds(self) -> float:
        """CPU时间转换为秒"""
        return self.cpu_time_ms / 1000.0
    
    @property
    def output_limit_bytes(self) -> int:
        """输出限制转换为字节"""
        return int(self.output_limit_kb * 1024)


@dataclass
class ExecutionResult:
    """执行结果"""
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0
    elapsed_time_ms: float = 0.0      # 实际运行时间 (ms)
    peak_memory_mb: float = 0.0       # 峰值内存 (MB)
    output_size_bytes: int = 0        # 输出大小 (字节)
    
    # 判定结果
    tle: bool = False                 # 时间超限
    mle: bool = False                 # 内存超限
    ole: bool = False                 # 输出超限
    re: bool = False                  # 运行时错误
    
    # 限制信息
    time_limit_ms: float = 0.0       # 时间限制
    memory_limit_mb: float = 0.0     # 内存限制
    output_limit_kb: float = 64.0    # 输出限制
    
    @property
    def time_ratio(self) -> float:
        """时间使用比例"""
        if self.time_limit_ms > 0:
            return self.elapsed_time_ms / self.time_limit_ms
        return 0.0
    
    @property
    def memory_ratio(self) -> float:
        """内存使用比例"""
        if self.memory_limit_mb > 0:
            return self.peak_memory_mb / self.memory_limit_mb
        return 0.0
    
    @property
    def is_accepted(self) -> bool:
        """是否通过"""
        return not self.tle and not self.mle and not self.ole and not self.re and self.returncode == 0
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'stdout': self.stdout,
            'stderr': self.stderr,
            'returncode': self.returncode,
            'elapsed_time_ms': round(self.elapsed_time_ms, 2),
            'peak_memory_mb': round(self.peak_memory_mb, 2),
            'output_size_bytes': self.output_size_bytes,
            'tle': self.tle,
            'mle': self.mle,
            'ole': self.ole,
            're': self.re,
            'time_limit_ms': self.time_limit_ms,
            'memory_limit_mb': self.memory_limit_mb,
            'output_limit_kb': self.output_limit_kb,
            'time_ratio': round(self.time_ratio, 4),
            'memory_ratio': round(self.memory_ratio, 4),
            'is_accepted': self.is_accepted,
        }
    
    def to_judge_string(self) -> str:
        """转换为评测结果字符串"""
        if self.tle:
            return f"Time:{int(self.elapsed_time_ms)}\nTimeout"
        elif self.mle:
            return f"Memory:{self.peak_memory_mb:.1f}\nMemory Limit Exceeded"
        elif self.ole:
            return f"Output:{self.output_size_bytes}\nOutput Limit Exceeded"
        elif self.re:
            return f"Runtime Error\n{self.stderr}"
        else:
            return f"Time:{int(self.elapsed_time_ms)}\nMemory:{self.peak_memory_mb:.1f}"


class ResourceMonitor:
    """资源监控器 - 实时监控资源使用"""
    
    def __init__(self, limits: ResourceLimits):
        self.limits = limits
        self.start_time: Optional[float] = None
        self.start_cpu_time: Optional[float] = None
        self.peak_memory: int = 0
        self._monitor_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._force_stop = threading.Event()
    
    def start(self):
        """开始监控"""
        self.start_time = time.time()
        self.start_cpu_time = time.process_time()
        self.peak_memory = self._get_current_memory()
        self._stop_event.clear()
        self._force_stop.clear()
        
        # 启动监控线程 (每2ms检查一次，满足2-3ms精度要求)
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()
    
    def stop(self) -> Dict[str, Any]:
        """停止监控并返回统计信息"""
        self._stop_event.set()
        if self._monitor_thread:
            self._monitor_thread.join(timeout=1.0)
        
        end_time = time.time()
        end_cpu_time = time.process_time()
        
        elapsed_ms = (end_time - self.start_time) * 1000
        cpu_ms = (end_cpu_time - self.start_cpu_time) * 1000
        
        # 判断TLE：实际运行时间超过限制
        tle = elapsed_ms > self.limits.time_ms
        
        # 判断MLE：峰值内存超过限制（不含冗余）
        mle = self.peak_memory > self.limits.memory_bytes
        
        # 判断是否被强制终止（超过最大允许时间）
        force_terminated = elapsed_ms >= self.limits.max_time_ms
        
        return {
            'elapsed_time_ms': elapsed_ms,
            'cpu_time_ms': cpu_ms,
            'peak_memory_bytes': self.peak_memory,
            'peak_memory_mb': self.peak_memory / (1024 * 1024),
            'tle': tle,
            'mle': mle,
            'force_terminated': force_terminated,
            'within_max_time': elapsed_ms < self.limits.max_time_ms,
        }
    
    def _monitor_loop(self):
        """监控循环"""
        while not self._stop_event.is_set():
            current_memory = self._get_current_memory()
            self.peak_memory = max(self.peak_memory, current_memory)
            
            # 检查内存限制（不含冗余，严格判定）
            if current_memory > self.limits.memory_bytes:
                self._force_stop.set()
                raise MemoryLimitExceeded(
                    f"MLE: {current_memory / (1024*1024):.2f} MB > {self.limits.memory_mb} MB"
                )
            
            # 检查最大允许时间（含冗余，强制终止）
            current_time = time.time()
            elapsed_ms = (current_time - self.start_time) * 1000
            if elapsed_ms >= self.limits.max_time_ms:
                self._force_stop.set()
                # 不抛出异常，让调用方处理
            
            self._stop_event.wait(0.002)  # 2ms检查间隔
    
    def _get_current_memory(self) -> int:
        """获取当前内存使用 (字节)"""
        if sys.platform == 'win32':
            try:
                import psutil
                process = psutil.Process(os.getpid())
                return process.memory_info().rss
            except ImportError:
                return 0
        else:
            usage = resource.getrusage(resource.RUSAGE_SELF)
            return usage.ru_maxrss * 1024
    
    def check_output_limit(self, output_bytes: int) -> bool:
        """检查输出是否超限"""
        return output_bytes > self.limits.output_limit_bytes


def set_resource_limits(limits: ResourceLimits):
    """设置系统资源限制 (Unix/Linux)"""
    if sys.platform == 'win32':
        return
    
    # 设置内存限制 (RLIMIT_AS)
    try:
        resource.setrlimit(
            resource.RLIMIT_AS,
            (limits.memory_bytes_with_buffer, limits.memory_bytes_with_buffer)
        )
    except (ValueError, OSError):
        pass
    
    # 设置CPU时间限制 (RLIMIT_CPU) - 使用最大允许时间
    try:
        resource.setrlimit(
            resource.RLIMIT_CPU,
            (int(limits.max_time_seconds), int(limits.max_time_seconds))
        )
    except (ValueError, OSError):
        pass
    
    # 设置栈大小限制 (RLIMIT_STACK)
    try:
        resource.setrlimit(
            resource.RLIMIT_STACK,
            (limits.stack_bytes, limits.stack_bytes)
        )
    except (ValueError, OSError):
        pass
    
    # 设置文件大小限制 (RLIMIT_FSIZE) - 100MB
    try:
        resource.setrlimit(
            resource.RLIMIT_FSIZE,
            (100 * 1024 * 1024, 100 * 1024 * 1024)
        )
    except (ValueError, OSError):
        pass
    
    # 设置进程数限制 (RLIMIT_NPROC)
    try:
        resource.setrlimit(
            resource.RLIMIT_NPROC,
            (64, 64)
        )
    except (ValueError, OSError):
        pass


def set_time_limit_signal(seconds: float):
    """设置超时信号 (Unix/Linux) - 使用最大允许时间"""
    if sys.platform == 'win32':
        return
    
    def timeout_handler(signum, frame):
        # 不抛出异常，让监控线程处理
        pass
    
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(int(seconds) + 1)  # 额外1秒缓冲


@contextmanager
def resource_limit_context(limits: ResourceLimits):
    """
    资源限制上下文管理器
    
    使用方法:
        with resource_limit_context(ResourceLimits(memory_mb=256, time_ms=1000)) as monitor:
            # 执行代码
            pass
    """
    # 设置系统资源限制
    set_resource_limits(limits)
    
    # 设置超时信号（使用最大允许时间）
    set_time_limit_signal(limits.max_time_seconds)
    
    # 创建监控器
    monitor = ResourceMonitor(limits)
    monitor.start()
    
    try:
        yield monitor
    finally:
        # 停止监控
        stats = monitor.stop()
        
        # 取消超时信号
        if sys.platform != 'win32':
            signal.alarm(0)
        
        # 验证内存限制
        if not stats['within_max_time']:
            # 超过最大允许时间，强制终止
            pass


class OutputLimitChecker:
    """输出限制检查器"""
    
    def __init__(self, limit_kb: float = 64.0):
        self.limit_bytes = int(limit_kb * 1024)
        self.output_buffer: list = []
        self.total_bytes: int = 0
    
    def write(self, data: str) -> bool:
        """写入输出数据，返回是否超限"""
        data_bytes = len(data.encode('utf-8'))
        self.total_bytes += data_bytes
        self.output_buffer.append(data)
        return self.total_bytes > self.limit_bytes
    
    def get_output(self) -> str:
        """获取完整输出"""
        return ''.join(self.output_buffer)
    
    def is_over_limit(self) -> bool:
        """检查是否超限"""
        return self.total_bytes > self.limit_bytes
    
    def get_usage_ratio(self) -> float:
        """获取使用比例"""
        return self.total_bytes / self.limit_bytes if self.limit_bytes > 0 else 0


class ResourceLimitDecorator:
    """资源限制装饰器"""
    
    def __init__(self, memory_mb: float = 256.0, time_ms: float = 1000.0, output_kb: float = 64.0):
        self.limits = ResourceLimits(
            memory_mb=memory_mb,
            time_ms=time_ms,
            output_limit_kb=output_kb,
        )
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with resource_limit_context(self.limits) as monitor:
                result = func(*args, **kwargs)
            return result
        return wrapper


# 预定义的资源限制配置
DEFAULT_LIMITS = ResourceLimits(
    memory_mb=256.0,
    time_ms=1000.0,
    stack_mb=64.0,
    cpu_time_ms=1000.0,
    memory_buffer_mb=8.0,
    output_limit_kb=64.0,
)

# 常用限制配置
MEMORY_LIMITS = {
    'low': ResourceLimits(memory_mb=64.0, time_ms=1000.0, memory_buffer_mb=8.0),
    'medium': ResourceLimits(memory_mb=256.0, time_ms=1000.0, memory_buffer_mb=8.0),
    'high': ResourceLimits(memory_mb=512.0, time_ms=1000.0, memory_buffer_mb=8.0),
    'unlimited': ResourceLimits(memory_mb=1024.0, time_ms=5000.0, memory_buffer_mb=8.0),
}

TIME_LIMITS = {
    'fast': ResourceLimits(memory_mb=256.0, time_ms=500.0),
    'normal': ResourceLimits(memory_mb=256.0, time_ms=1000.0),
    'slow': ResourceLimits(memory_mb=256.0, time_ms=2000.0),
    'interactive': ResourceLimits(memory_mb=256.0, time_ms=10000.0),
}


def get_resource_stats() -> Dict[str, Any]:
    """获取当前进程的资源使用统计"""
    stats = {
        'pid': os.getpid(),
        'platform': sys.platform,
    }
    
    if sys.platform == 'win32':
        try:
            import psutil
            process = psutil.Process(os.getpid())
            mem_info = process.memory_info()
            stats['memory_rss_mb'] = mem_info.rss / (1024 * 1024)
            stats['memory_vms_mb'] = mem_info.vms / (1024 * 1024)
        except ImportError:
            stats['memory_rss_mb'] = 0
            stats['memory_vms_mb'] = 0
    else:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        stats['memory_rss_mb'] = usage.ru_maxrss / 1024
        stats['user_time_ms'] = usage.ru_utime * 1000
        stats['system_time_ms'] = usage.ru_stime * 1000
    
    return stats
