# judge/strategies/go_special.py
"""
Go Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class GoSpecialJudgeClient(SpecialJudgeClient):
    """Go Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/spj",
            judge_file
        ]


class GoInteractiveClient(InteractiveJudgeClient):
    """Go 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
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
            'go', 'build',
            '-o', f"{work_dir}/interact",
            interact_file
        ]


class GoO1SpecialJudgeClient(SpecialJudgeClient):
    """Go O1 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O1)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', f"{work_dir}/main",
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', f"{work_dir}/spj",
            judge_file
        ]


class GoO2SpecialJudgeClient(SpecialJudgeClient):
    """Go O2 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O2)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/spj",
            judge_file
        ]


class GoO3SpecialJudgeClient(SpecialJudgeClient):
    """Go O3 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O3)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', f"{work_dir}/main",
            source_file
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', f"{work_dir}/spj",
            judge_file
        ]


class GoO1InteractiveClient(InteractiveJudgeClient):
    """Go O1 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O1)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', f"{work_dir}/main",
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
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', f"{work_dir}/interact",
            interact_file
        ]


class GoO2InteractiveClient(InteractiveJudgeClient):
    """Go O2 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O2)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
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
            'go', 'build',
            '-o', f"{work_dir}/interact",
            interact_file
        ]


class GoO3InteractiveClient(InteractiveJudgeClient):
    """Go O3 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O3)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', f"{work_dir}/main",
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
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', f"{work_dir}/interact",
            interact_file
        ]
