# judge/strategies/cpp.py
from .base import BaseJudgeClient
from typing import List, Optional


class JudgeClient(BaseJudgeClient):
    def __init__(self) -> None:
        super().__init__()

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return [
            exec_file
        ]

    @property
    def extension_name(self) -> str:
        return '.cpp'

    @property
    def language_name(self) -> str:
        return 'cpp17(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            'g++', source_file, '-o', f"{work_dir}/main",
            '-O2',
            'std=c++17',
            '-DONLINE_JUDGE',
            '-Wall'
            ]
