# judge/strategies/rust.py
from .base import BaseJudgeClient
from typing import List, Optional


class RustJudgeClient(BaseJudgeClient):
    """Rust 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '--edition', '2021'
        ]


class RustO1JudgeClient(BaseJudgeClient):
    """Rust O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=1',
            '--edition', '2021'
        ]


class RustO2JudgeClient(BaseJudgeClient):
    """Rust O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=2',
            '--edition', '2021'
        ]


class RustO3JudgeClient(BaseJudgeClient):
    """Rust O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.rs'

    @property
    def language_name(self) -> str:
        return 'rust(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'rustc', source_file,
            '-o', f"{work_dir}/main",
            '-C', 'opt-level=3',
            '--edition', '2021'
        ]
