# judge/strategies/csharp_special.py
"""
C# Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class CSharpSpecialJudgeClient(SpecialJudgeClient):
    """C# Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            judge_file
        ]


class CSharpInteractiveClient(InteractiveJudgeClient):
    """C# 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            source_file
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'dotnet', 'build',
            '-c', 'Release',
            '-o', work_dir,
            interact_file
        ]


class CSharpMonoSpecialJudgeClient(SpecialJudgeClient):
    """C# (Mono) Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['mono', exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp(mono)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', f"{work_dir}/main.exe",
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return ['mono', f"{work_dir}/spj.exe", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', f"{work_dir}/spj.exe",
            judge_file
        ]


class CSharpMonoInteractiveClient(InteractiveJudgeClient):
    """C# (Mono) 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['mono', exec_file]

    @property
    def extension_name(self) -> str:
        return '.cs'

    @property
    def language_name(self) -> str:
        return 'csharp(mono)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', f"{work_dir}/main.exe",
            source_file
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return ['mono', f"{work_dir}/interact.exe"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'mcs',
            '-out:', f"{work_dir}/interact.exe",
            interact_file
        ]
