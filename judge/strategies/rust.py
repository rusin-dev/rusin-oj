# judge/strategies/rust.py
from .base import BaseJudgeClient
from ..utils.resource_limiter import ResourceLimits
from typing import List, Optional


class RustJudgeClient(BaseJudgeClient):
    """Rust 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Rust默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Rust程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', self._output_path(work_dir),
            '--edition', '2021'
        ]


class RustO1JudgeClient(BaseJudgeClient):
    """Rust O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Rust默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Rust程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', self._output_path(work_dir),
            '-C', 'opt-level=1',
            '--edition', '2021'
        ]


class RustO2JudgeClient(BaseJudgeClient):
    """Rust O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Rust默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Rust程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', self._output_path(work_dir),
            '-C', 'opt-level=2',
            '--edition', '2021'
        ]


class RustO3JudgeClient(BaseJudgeClient):
    """Rust O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Rust默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Rust程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', self._output_path(work_dir),
            '-C', 'opt-level=3',
            '--edition', '2021'
        ]
