# judge/strategies/python.py
import sys
from .base import BaseJudgeClient
from typing import List, Optional
from ..utils.resource_limiter import ResourceLimits

IS_WINDOWS = sys.platform == 'win32'


class JudgeClient(BaseJudgeClient):
    def __init__(self) -> None:
        super().__init__()

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Python默认资源限制"""
        return ResourceLimits(
            memory_mb=256.0,
            time_ms=1000.0,
            stack_mb=32.0,
            cpu_time_ms=1000.0,
        )

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        python_cmd = 'python' if IS_WINDOWS else 'python3'
        return [python_cmd, exec_file]

    @property
    def extension_name(self) -> str:
        return '.py'

    @property
    def language_name(self) -> str:
        return 'python3'

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return None
