# judge/strategies/csharp.py
from .base import BaseJudgeClient
from typing import List, Optional


class CSharpJudgeClient(BaseJudgeClient):
    """C# (.NET)"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp'

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

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', f"{work_dir}/main.exe",
            source_file
        ]
