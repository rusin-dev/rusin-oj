# judge/strategies/c_special.py
"""
C Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class C99SpecialJudgeClient(SpecialJudgeClient):
    """C99 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c99(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c99',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        judge_file = self._validate_judge_file(judge_file)
        input_file = self._validate_input_file(input_file)
        output_file = self._validate_output_file(output_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        judge_file = self._validate_judge_file(judge_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', judge_file, '-o', f"{work_dir}/spj",
            '-std=c99',
            '-Wall'
        ]


class C99InteractiveClient(InteractiveJudgeClient):
    """C99 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c99(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c99',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'gcc', interact_file, '-o', f"{work_dir}/interact",
            '-std=c99',
            '-Wall'
        ]


class C11SpecialJudgeClient(SpecialJudgeClient):
    """C11 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c11(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        judge_file = self._validate_judge_file(judge_file)
        input_file = self._validate_input_file(input_file)
        output_file = self._validate_output_file(output_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        judge_file = self._validate_judge_file(judge_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', judge_file, '-o', f"{work_dir}/spj",
            '-std=c11',
            '-Wall'
        ]


class C11InteractiveClient(InteractiveJudgeClient):
    """C11 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c11(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c11',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'gcc', interact_file, '-o', f"{work_dir}/interact",
            '-std=c11',
            '-Wall'
        ]


class C17SpecialJudgeClient(SpecialJudgeClient):
    """C17 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c17(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c17',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        judge_file = self._validate_judge_file(judge_file)
        input_file = self._validate_input_file(input_file)
        output_file = self._validate_output_file(output_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        judge_file = self._validate_judge_file(judge_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', judge_file, '-o', f"{work_dir}/spj",
            '-std=c17',
            '-Wall'
        ]


class C17InteractiveClient(InteractiveJudgeClient):
    """C17 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c17(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c17',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'gcc', interact_file, '-o', f"{work_dir}/interact",
            '-std=c17',
            '-Wall'
        ]


class C23SpecialJudgeClient(SpecialJudgeClient):
    """C23 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c23(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        judge_file = self._validate_judge_file(judge_file)
        input_file = self._validate_input_file(input_file)
        output_file = self._validate_output_file(output_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        judge_file = self._validate_judge_file(judge_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'gcc', judge_file, '-o', f"{work_dir}/spj",
            '-std=c23',
            '-Wall'
        ]


class C23InteractiveClient(InteractiveJudgeClient):
    """C23 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.c'

    @property
    def language_name(self) -> str:
        return 'c23(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'gcc', source_file, '-o', f"{work_dir}/main",
            '-std=c23',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'gcc', interact_file, '-o', f"{work_dir}/interact",
            '-std=c23',
            '-Wall'
        ]
