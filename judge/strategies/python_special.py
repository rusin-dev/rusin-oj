# judge/strategies/python_special.py
"""
Python Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class PythonSpecialJudgeClient(SpecialJudgeClient):
    """Python Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['python3', exec_file]

    @property
    def extension_name(self) -> str:
        return '.py'

    @property
    def language_name(self) -> str:
        return 'python3(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return None

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return ['python3', judge_file, input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return None


class PythonInteractiveClient(InteractiveJudgeClient):
    """Python 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ['python3', exec_file]

    @property
    def extension_name(self) -> str:
        return '.py'

    @property
    def language_name(self) -> str:
        return 'python3(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return None

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return ['python3', interact_file]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return None
