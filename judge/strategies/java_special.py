# judge/strategies/java_special.py
"""
Java Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class JavaSpecialJudgeClient(SpecialJudgeClient):
    """Java Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['java', '-cp', work_dir, 'Main']

    @property
    def extension_name(self) -> str:
        return '.java'

    @property
    def language_name(self) -> str:
        return 'java(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'javac', source_file,
            '-d', work_dir,
            '-encoding', 'UTF-8'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return ['java', '-cp', work_dir, 'SpecialJudge', input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'javac', judge_file,
            '-d', work_dir,
            '-encoding', 'UTF-8'
        ]


class JavaInteractiveClient(InteractiveJudgeClient):
    """Java 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['java', '-cp', work_dir, 'Main']

    @property
    def extension_name(self) -> str:
        return '.java'

    @property
    def language_name(self) -> str:
        return 'java(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'javac', source_file,
            '-d', work_dir,
            '-encoding', 'UTF-8'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return ['java', '-cp', work_dir, 'Interactor']

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'javac', interact_file,
            '-d', work_dir,
            '-encoding', 'UTF-8'
        ]
