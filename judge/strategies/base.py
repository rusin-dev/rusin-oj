# judge/strategies/base.py
from abc import ABC, abstractmethod
from typing import List, Optional

from ..utils.path_validator import (
    validate_source_file,
    validate_work_dir,
    validate_file_path,
    PathValidationError,
)


class BaseJudgeClient(ABC):
    """判题客户端基类"""

    def __init__(self) -> None:
        super().__init__()

    def _validate_exec_file(self, exec_file: str, work_dir: str) -> str:
        """验证执行文件路径"""
        return validate_file_path(exec_file, work_dir)

    def _validate_source_file(self, source_file: str) -> str:
        """验证源文件路径"""
        return validate_source_file(source_file)

    def _validate_work_dir(self, work_dir: str) -> str:
        """验证工作目录路径"""
        return validate_work_dir(work_dir)

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


class SpecialJudgeClient(BaseJudgeClient):
    """
    Special Judge 判题客户端基类
    用于答案不唯一或需要特殊验证的题目
    """

    def _validate_judge_file(self, judge_file: str) -> str:
        """验证Special Judge文件路径"""
        return validate_source_file(judge_file)

    def _validate_input_file(self, input_file: str) -> str:
        """验证输入文件路径"""
        return validate_file_path(input_file)

    def _validate_output_file(self, output_file: str) -> str:
        """验证输出文件路径"""
        return validate_file_path(output_file)

    @abstractmethod
    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        """
        返回 Special Judge 执行命令

        Args:
            judge_file: Special Judge 程序文件路径
            input_file: 题目输入文件路径
            output_file: 用户程序输出文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表
            例如: ['./spj', 'input.txt', 'output.txt']
        """

    @abstractmethod
    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回 Special Judge 程序编译命令

        Args:
            judge_file: Special Judge 源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None
            例如: ['g++', 'spj.cpp', '-o', 'spj']
        """

    @property
    def judge_extension(self) -> str:
        """
        返回 Special Judge 程序的扩展名
        默认与主程序相同
        """
        return self.extension_name


class InteractiveJudgeClient(BaseJudgeClient):
    """
    交互题判题客户端基类
    用于需要与评测程序进行交互的题目
    """

    def _validate_interact_file(self, interact_file: str) -> str:
        """验证交互评测程序文件路径"""
        return validate_source_file(interact_file)

    @abstractmethod
    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        """
        返回交互题执行命令

        Args:
            exec_file: 用户程序可执行文件路径
            interact_file: 交互评测程序文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表
        """

    @abstractmethod
    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        """
        返回交互评测程序编译命令

        Args:
            interact_file: 交互评测程序源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None
        """

    @property
    def interact_extension(self) -> str:
        """
        返回交互评测程序的扩展名
        默认与主程序相同
        """
        return self.extension_name

    @property
    def default_timeout(self) -> int:
        """
        返回默认超时时间（秒）
        交互题通常需要更长的超时时间
        """
        return 10