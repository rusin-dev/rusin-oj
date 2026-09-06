# judge/strategies/python.py
from .base import BaseJudgeClient
from typing import List, Optional
from ..utils.resource_limiter import ResourceLimits


class JudgeClient(BaseJudgeClient):
    def __init__(self) -> None:
        super().__init__()

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Python默认资源限制"""
        return ResourceLimits(
            memory_mb=256.0,   # Python解释器+程序内存
            time_ms=1000.0,    # 1秒
            stack_mb=32.0,     # Python栈较小
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        exec_file = self._validate_exec_file(exec_file, work_dir)
        return ['python3', exec_file]

    @property
    def extension_name(self) -> str:
        return '.py'

    @property
    def language_name(self) -> str:
        return 'python3'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return None