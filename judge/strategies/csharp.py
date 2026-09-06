# judge/strategies/csharp.py
from .base import BaseJudgeClient
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

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'mcs',
            '-out:', f"{work_dir}/main.exe",
            source_file
        ]
