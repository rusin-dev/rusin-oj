# judge/strategies/go.py
from .base import BaseJudgeClient
from typing import List, Optional


class GoJudgeClient(BaseJudgeClient):
    """Go 无优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
            source_file
        ]


class GoO1JudgeClient(BaseJudgeClient):
    """Go O1 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O1)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'go', 'build',
            '-gcflags', '-N -l',
            '-o', f"{work_dir}/main",
            source_file
        ]


class GoO2JudgeClient(BaseJudgeClient):
    """Go O2 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O2)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'go', 'build',
            '-o', f"{work_dir}/main",
            source_file
        ]


class GoO3JudgeClient(BaseJudgeClient):
    """Go O3 优化"""

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return [exec_file]

    @property
    def extension_name(self) -> str:
        return '.go'

    @property
    def language_name(self) -> str:
        return 'go(with O3)'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            'go', 'build',
            '-ldflags', '-s -w',
            '-o', f"{work_dir}/main",
            source_file
        ]
