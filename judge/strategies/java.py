# judge/strategies/java.py
from .base import BaseJudgeClient
from typing import List, Optional

class JudgeClient(BaseJudgeClient):
    @property
    def language_name(self) -> str:
        return "java"

    @property
    def file_extension(self) -> str:
        return ".java"

    @property
    def source_filename(self) -> str:
        return "Main.java"

    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        return [
            "javac",
            source_file,
            "-d", work_dir,
            "-encoding", "UTF-8"
        ]

    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        return ["java", "-cp", work_dir, "Main"]
