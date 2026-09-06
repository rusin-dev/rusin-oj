# judge/strategies/java.py
from .base import BaseJudgeClient
from typing import List, Optional
from ..utils.resource_limiter import ResourceLimits


class JudgeClient(BaseJudgeClient):
    @property
    def default_resource_limits(self) -> ResourceLimits:
        """Java默认资源限制 (JVM需要更多内存)"""
        return ResourceLimits(
            memory_mb=512.0,   # JVM + 程序内存
            time_ms=2000.0,    # 2秒 (JVM启动较慢)
            stack_mb=64.0,
            cpu_time_ms=2000.0,
        )

    @property
    def language_name(self) -> str:
        return "java"

    @property
    def extension_name(self) -> str:
        return ".java"

    @property
    def source_filename(self) -> str:
        return "Main.java"

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        source_file = self._validate_source_file(source_file)
        work_dir = self._validate_work_dir(work_dir)
        return [
            "javac",
            source_file,
            "-d", work_dir,
            "-encoding", "UTF-8"
        ]

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        work_dir = self._validate_work_dir(work_dir)
        return ["java", "-cp", work_dir, "Main"]
