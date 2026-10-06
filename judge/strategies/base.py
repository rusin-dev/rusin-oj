# judge/strategies/base.py
from abc import ABC, abstractmethod
from typing import List, Optional
import sys

IS_WINDOWS = sys.platform == 'win32'


class BaseJudgeClient(ABC):
    """
    判题客户端基类
    定义了编译和执行用户程序的基本接口
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def exe_suffix(self) -> str:
        """返回可执行文件后缀"""
        return '.exe' if IS_WINDOWS else ''

    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        """
        返回执行用户程序的命令

        Args:
            exec_file: 可执行文件的完整路径
            work_dir: 工作目录路径

        Returns:
            执行命令列表，例如: ['./main', 'arg1', 'arg2']
        """

    @property
    @abstractmethod
    def extension_name(self) -> str:
        """
        返回源代码文件扩展名

        Returns:
            文件扩展名，例如: '.py', '.cpp', '.java'
        """

    @property
    @abstractmethod
    def language_name(self) -> str:
        """
        返回语言名称标识符

        Returns:
            语言名称，例如: 'python3', 'cpp17', 'java'
        """

    @abstractmethod
    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回编译源代码的命令

        Args:
            source_file: 源代码文件的完整路径
            work_dir: 工作目录路径

        Returns:
            编译命令列表，如果无需编译（解释型语言）返回 None
        """

    def _output_path(self, work_dir: str) -> str:
        """返回可执行文件输出路径（自动添加平台后缀）"""
        return f"{work_dir}/main{self.exe_suffix}"
