# judge/strategies/cpp_interactive.py
"""
C++ 交互题策略类
用于需要与评测程序进行交互的题目
"""
from .base import InteractiveJudgeClient
from typing import List, Optional


class Cpp98InteractiveClient(InteractiveJudgeClient):
    """C++98 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp98(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++98',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++98',
            '-Wall'
        ]


class Cpp11InteractiveClient(InteractiveJudgeClient):
    """C++11 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++11',
            '-Wall'
        ]


class Cpp14InteractiveClient(InteractiveJudgeClient):
    """C++14 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp14(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++14',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++14',
            '-Wall'
        ]


class Cpp17InteractiveClient(InteractiveJudgeClient):
    """C++17 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp17(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++17',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++17',
            '-Wall'
        ]


class Cpp20InteractiveClient(InteractiveJudgeClient):
    """C++20 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++20',
            '-Wall'
        ]


class Cpp23InteractiveClient(InteractiveJudgeClient):
    """C++23 交互题"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23(interactive)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-DINTERACTIVE',
            '-Wall'
        ]

    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [f"{work_dir}/interact"]

    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        interact_file = self._validate_interact_file(interact_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'g++', interact_file, '-o', f"{work_dir}/interact",
            '-std=c++23',
            '-Wall'
        ]
