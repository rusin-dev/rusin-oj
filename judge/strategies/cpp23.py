# judge/strategies/cpp23.py
from .base import BaseJudgeClient
from ..utils.resource_limiter import ResourceLimits
from typing import List, Optional


class Cpp23JudgeClient(BaseJudgeClient):
    """C++23 无优化"""

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C/C++默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # 编译后程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,     # C/C++栈较大
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', self._output_path(work_dir),
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp23O1JudgeClient(BaseJudgeClient):
    """C++23 O1 优化"""

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C/C++默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # 编译后程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,     # C/C++栈较大
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', self._output_path(work_dir),
            '-O1',
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp23O2JudgeClient(BaseJudgeClient):
    """C++23 O2 优化"""

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C/C++默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # 编译后程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,     # C/C++栈较大
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', self._output_path(work_dir),
            '-O2',
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp23O3JudgeClient(BaseJudgeClient):
    """C++23 O3 优化"""

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C/C++默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # 编译后程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,     # C/C++栈较大
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', self._output_path(work_dir),
            '-O3',
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]
