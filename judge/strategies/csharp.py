# judge/strategies/csharp.py
from .base import BaseJudgeClient
from ..utils.resource_limiter import ResourceLimits
from typing import List, Optional


class CSharpJudgeClient(BaseJudgeClient):
    """C# (.NET)"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp'

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C# (.NET) 默认资源限制"""
        return ResourceLimits(
            memory_mb=256.0,   # .NET运行时内存
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            source_file
        ]


class CSharpMonoJudgeClient(BaseJudgeClient):
    """C# (Mono)"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return ['mono', exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp(mono)'

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """C# (Mono) 默认资源限制"""
        return ResourceLimits(
            memory_mb=192.0,   # Mono运行时内存较小
            time_ms=1000.0,    # 1秒
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'mcs',
            '-out:', f"{work_dir}/main.exe",
            source_file
        ]
