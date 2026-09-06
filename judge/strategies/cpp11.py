# judge/strategies/cpp11.py
from .base import BaseJudgeClient
from typing import List, Optional


class Cpp11JudgeClient(BaseJudgeClient):
    """C++11 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp11O1JudgeClient(BaseJudgeClient):
    """C++11 O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O1',
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp11O2JudgeClient(BaseJudgeClient):
    """C++11 O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O2',
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]


class Cpp11O3JudgeClient(BaseJudgeClient):
    """C++11 O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O3',
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]
