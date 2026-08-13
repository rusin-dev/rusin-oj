# judge/strategies/base.py
from abc import ABC, abstractmethod
from typing import List, Optional


class BaseJudgeClient(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        """
        返回执行命令
        exec_command() -> ['python3', source]
        """

    @property
    @abstractmethod
    def extension_name(self) -> str:
        """
        返回扩展名名称
        """

    @property
    @abstractmethod
    def language_name(self) -> str:
        """
        返回语言名称
        """

    @abstractmethod
    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回编译命令
        comp_command() -> ['gcc', source, '-o', source]
        """