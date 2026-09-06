# judge/strategies/cpp20.py
from .base import BaseJudgeClient
from typing import List, Optional


class Cpp20JudgeClient(BaseJudgeClient):
    """C++20 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp20O1JudgeClient(BaseJudgeClient):
    """C++20 O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O1',
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp20O2JudgeClient(BaseJudgeClient):
    """C++20 O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O2',
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp20O3JudgeClient(BaseJudgeClient):
    """C++20 O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O3',
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-Wall'
        ]
