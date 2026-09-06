# judge/strategies/csharp.py
from .base import BaseJudgeClient
from ..utils.resource_limiter import ResourceLimits
from typing import List, Optional


class CSharpJudgeClient(BaseJudgeClient):
    """C# (.NET)"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['dotnet', 'exec', f"{work_dir}/test.dll"]

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
            memory_mb=256.0,
            time_ms=1000.0,
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            source_file
        ]


class CSharpMonoJudgeClient(BaseJudgeClient):
    """C# (Mono)"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
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
            memory_mb=192.0,
            time_ms=1000.0,
            stack_mb=64.0,
            cpu_time_ms=1000.0,
        )

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', self._output_path(work_dir),
            source_file
        ]
