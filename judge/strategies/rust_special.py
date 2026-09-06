# judge/strategies/rust_special.py
"""
Rust Special Judge 和交互题策略类
"""
from .base import SpecialJudgeClient, InteractiveJudgeClient
from typing import List, Optional


class RustSpecialJudgeClient(SpecialJudgeClient):
    """Rust Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '--edition', '2021'
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
            'rustc', judge_file,
            '-o', f"{work_dir}/spj",
            '--edition', '2021'
        ]


class RustInteractiveClient(InteractiveJudgeClient):
    """Rust 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '--edition', '2021'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'rustc', interact_file,
            '-o', f"{work_dir}/interact",
            '--edition', '2021'
        ]


class RustO1SpecialJudgeClient(SpecialJudgeClient):
    """Rust O1 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O1)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=1',
            '--edition', '2021'
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
            'rustc', judge_file,
            '-o', f"{work_dir}/spj",
            '-C', 'opt-level=1',
            '--edition', '2021'
        ]


class RustO2SpecialJudgeClient(SpecialJudgeClient):
    """Rust O2 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O2)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=2',
            '--edition', '2021'
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
            'rustc', judge_file,
            '-o', f"{work_dir}/spj",
            '-C', 'opt-level=2',
            '--edition', '2021'
        ]


class RustO3SpecialJudgeClient(SpecialJudgeClient):
    """Rust O3 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O3)(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=3',
            '--edition', '2021'
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
            'rustc', judge_file,
            '-o', f"{work_dir}/spj",
            '-C', 'opt-level=3',
            '--edition', '2021'
        ]


class RustO1InteractiveClient(InteractiveJudgeClient):
    """Rust O1 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O1)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=1',
            '--edition', '2021'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'rustc', interact_file,
            '-o', f"{work_dir}/interact",
            '-C', 'opt-level=1',
            '--edition', '2021'
        ]


class RustO2InteractiveClient(InteractiveJudgeClient):
    """Rust O2 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O2)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=2',
            '--edition', '2021'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'rustc', interact_file,
            '-o', f"{work_dir}/interact",
            '-C', 'opt-level=2',
            '--edition', '2021'
        ]


class RustO3InteractiveClient(InteractiveJudgeClient):
    """Rust O3 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O3)(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=3',
            '--edition', '2021'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        return [
            'rustc', interact_file,
            '-o', f"{work_dir}/interact",
            '-C', 'opt-level=3',
            '--edition', '2021'
        ]
