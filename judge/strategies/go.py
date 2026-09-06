# judge/strategies/go.py
from .base import BaseJudgeClient
from ..utils.resource_limiter import ResourceLimits
from typing import List, Optional


class GoJudgeClient(BaseJudgeClient):
    """Go 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Go默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Go程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', self._output_path(work_dir),
            source_file
        ]


class GoO1JudgeClient(BaseJudgeClient):
    """Go O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Go默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Go程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', self._output_path(work_dir),
            source_file
        ]


class GoO2JudgeClient(BaseJudgeClient):
    """Go O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Go默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Go程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', self._output_path(work_dir),
            source_file
        ]


class GoO3JudgeClient(BaseJudgeClient):
    """Go O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Go默认资源限制"""
        return ResourceLimits(
            memory_mb=128.0,   # Go程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', self._output_path(work_dir),
            source_file
        ]
