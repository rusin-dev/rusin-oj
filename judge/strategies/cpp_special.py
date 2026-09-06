# judge/strategies/cpp_special.py
"""
C++ Special Judge 策略类
用于答案不唯一或需要特殊验证的题目
"""
from .base import SpecialJudgeClient
from typing import List, Optional


class Cpp98SpecialJudgeClient(SpecialJudgeClient):
    """C++98 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp98(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++98',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++98',
            '-Wall'
        ]


class Cpp11SpecialJudgeClient(SpecialJudgeClient):
    """C++11 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp11(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++11',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++11',
            '-Wall'
        ]


class Cpp14SpecialJudgeClient(SpecialJudgeClient):
    """C++14 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp14(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++14',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++14',
            '-Wall'
        ]


class Cpp17SpecialJudgeClient(SpecialJudgeClient):
    """C++17 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp17(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++17',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++17',
            '-Wall'
        ]


class Cpp20SpecialJudgeClient(SpecialJudgeClient):
    """C++20 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp20(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++20',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++20',
            '-Wall'
        ]


class Cpp23SpecialJudgeClient(SpecialJudgeClient):
    """C++23 Special Judge"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp23(spj)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-std=c++23',
            '-DONLINE_JUDGE',
            '-Wall'
        ]

    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        return [f"{work_dir}/spj", input_file, output_file]

    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', judge_file, '-o', f"{work_dir}/spj",
            '-std=c++23',
            '-Wall'
        ]
