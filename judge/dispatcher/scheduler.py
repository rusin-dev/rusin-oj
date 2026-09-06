# judge/dispatcher/scheduler.py
"""
语言调度模块 - 根据语言名称和题目类型返回对应的判题策略实例

题目类型:
- normal: 普通判题
- spj: Special Judge（特殊判题）
- interactive: 交互题

流程: 前端传参 -> 中转站调度 -> 判题文件执行
"""
import json
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Type

from ..strategies.base import BaseJudgeClient
from ..strategies import (
    # Python
    PythonJudgeClient,
    # Java
    JavaJudgeClient,
    # C
    C99JudgeClient,
    C99O1JudgeClient,
    C99O2JudgeClient,
    C99O3JudgeClient,
    C11JudgeClient,
    C11O1JudgeClient,
    C11O2JudgeClient,
    C11O3JudgeClient,
    C17JudgeClient,
    C17O1JudgeClient,
    C17O2JudgeClient,
    C17O3JudgeClient,
    C23JudgeClient,
    C23O1JudgeClient,
    C23O2JudgeClient,
    C23O3JudgeClient,
    # C#
    CSharpJudgeClient,
    CSharpMonoJudgeClient,
    # C++98
    Cpp98JudgeClient,
    Cpp98O1JudgeClient,
    Cpp98O2JudgeClient,
    Cpp98O3JudgeClient,
    # C++11
    Cpp11JudgeClient,
    Cpp11O1JudgeClient,
    Cpp11O2JudgeClient,
    Cpp11O3JudgeClient,
    # C++14
    Cpp14JudgeClient,
    Cpp14O1JudgeClient,
    Cpp14O2JudgeClient,
    Cpp14O3JudgeClient,
    # C++17
    Cpp17JudgeClient,
    Cpp17O1JudgeClient,
    Cpp17O2JudgeClient,
    Cpp17O3JudgeClient,
    # C++20
    Cpp20JudgeClient,
    Cpp20O1JudgeClient,
    Cpp20O2JudgeClient,
    Cpp20O3JudgeClient,
    # C++23
    Cpp23JudgeClient,
    Cpp23O1JudgeClient,
    Cpp23O2JudgeClient,
    Cpp23O3JudgeClient,
    # Rust
    RustJudgeClient,
    RustO1JudgeClient,
    RustO2JudgeClient,
    RustO3JudgeClient,
    # Go
    GoJudgeClient,
    GoO1JudgeClient,
    GoO2JudgeClient,
    GoO3JudgeClient,
)


class ProblemType(Enum):
    """题目类型枚举"""
    NORMAL = "normal"           # 普通判题
    SPECIAL_JUDGE = "spj"       # Special Judge
    INTERACTIVE = "interactive" # 交互题


# 策略类注册表
STRATEGY_REGISTRY: Dict[str, Type[BaseJudgeClient]] = {
    # Python
    "python3": PythonJudgeClient,
    # Java
    "java": JavaJudgeClient,
    # C
    "c99": C99JudgeClient,
    "c99(with O1)": C99O1JudgeClient,
    "c99(with O2)": C99O2JudgeClient,
    "c99(with O3)": C99O3JudgeClient,
    "c11": C11JudgeClient,
    "c11(with O1)": C11O1JudgeClient,
    "c11(with O2)": C11O2JudgeClient,
    "c11(with O3)": C11O3JudgeClient,
    "c17": C17JudgeClient,
    "c17(with O1)": C17O1JudgeClient,
    "c17(with O2)": C17O2JudgeClient,
    "c17(with O3)": C17O3JudgeClient,
    "c23": C23JudgeClient,
    "c23(with O1)": C23O1JudgeClient,
    "c23(with O2)": C23O2JudgeClient,
    "c23(with O3)": C23O3JudgeClient,
    # C#
    "csharp": CSharpJudgeClient,
    "csharp(mono)": CSharpMonoJudgeClient,
    # C++98
    "cpp98": Cpp98JudgeClient,
    "cpp98(with O1)": Cpp98O1JudgeClient,
    "cpp98(with O2)": Cpp98O2JudgeClient,
    "cpp98(with O3)": Cpp98O3JudgeClient,
    # C++11
    "cpp11": Cpp11JudgeClient,
    "cpp11(with O1)": Cpp11O1JudgeClient,
    "cpp11(with O2)": Cpp11O2JudgeClient,
    "cpp11(with O3)": Cpp11O3JudgeClient,
    # C++14
    "cpp14": Cpp14JudgeClient,
    "cpp14(with O1)": Cpp14O1JudgeClient,
    "cpp14(with O2)": Cpp14O2JudgeClient,
    "cpp14(with O3)": Cpp14O3JudgeClient,
    # C++17
    "cpp17": Cpp17JudgeClient,
    "cpp17(with O1)": Cpp17O1JudgeClient,
    "cpp17(with O2)": Cpp17O2JudgeClient,
    "cpp17(with O3)": Cpp17O3JudgeClient,
    # C++20
    "cpp20": Cpp20JudgeClient,
    "cpp20(with O1)": Cpp20O1JudgeClient,
    "cpp20(with O2)": Cpp20O2JudgeClient,
    "cpp20(with O3)": Cpp20O3JudgeClient,
    # C++23
    "cpp23": Cpp23JudgeClient,
    "cpp23(with O1)": Cpp23O1JudgeClient,
    "cpp23(with O2)": Cpp23O2JudgeClient,
    "cpp23(with O3)": Cpp23O3JudgeClient,
    # Rust
    "rust": RustJudgeClient,
    "rust(with O1)": RustO1JudgeClient,
    "rust(with O2)": RustO2JudgeClient,
    "rust(with O3)": RustO3JudgeClient,
    # Go
    "go": GoJudgeClient,
    "go(with O1)": GoO1JudgeClient,
    "go(with O2)": GoO2JudgeClient,
    "go(with O3)": GoO3JudgeClient,
}


class JudgeRequest:
    """
    判题请求封装

    Attributes:
        language: 编程语言名称
        problem_type: 题目类型 (normal/spj/interactive)
        time_limit: 时间限制（毫秒）
        memory_limit: 内存限制（MB）
        judge_file: Special Judge 或交互程序文件路径（可选）
    """

    def __init__(
        self,
        language: str,
        problem_type: str = "normal",
        time_limit: int = 1000,
        memory_limit: int = 256,
        judge_file: Optional[str] = None,
    ):
        self.language = language
        self.problem_type = ProblemType(problem_type)
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.judge_file = judge_file

    def __repr__(self) -> str:
        return (
            f"JudgeRequest(language={self.language}, "
            f"type={self.problem_type.value}, "
            f"time={self.time_limit}ms, "
            f"mem={self.memory_limit}MB)"
        )


class JudgeResult:
    """
    判题结果封装

    Attributes:
        status: 判题状态 (accepted/wrong_answer/time_limit_exceeded/etc)
        time_used: 实际耗时（毫秒）
        memory_used: 实际内存使用（MB）
        output: 用户程序输出
        error: 错误信息
    """

    def __init__(
        self,
        status: str = "pending",
        time_used: int = 0,
        memory_used: int = 0,
        output: str = "",
        error: str = "",
    ):
        self.status = status
        self.time_used = time_used
        self.memory_used = memory_used
        self.output = output
        self.error = error

    def to_dict(self) -> Dict:
        return {
            "status": self.status,
            "time_used": self.time_used,
            "memory_used": self.memory_used,
            "output": self.output,
            "error": self.error,
        }


class Scheduler:
    """
    语言调度器

    根据前端传参（语言、题目类型、时间/内存限制）调度到对应的判题逻辑

    流程:
    1. 前端传参: language, problem_type, time_limit, memory_limit
    2. 中转站调度: 根据参数获取策略实例，组合判题逻辑
    3. 判题执行: 调用策略的 comp_command / exec_command
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        初始化调度器

        Args:
            config_path: 语言配置文件路径，默认为 config/languages.json
        """
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
        self._instances: Dict[str, BaseJudgeClient] = {}

    def _get_default_config_path(self) -> str:
        """获取默认配置文件路径"""
        return str(Path(__file__).parent.parent.parent / "config" / "languages.json")

    def _load_config(self) -> Dict:
        """加载语言配置"""
        config_path = Path(self.config_path)

        if not config_path.exists():
            return {"languages": {}, "available_languages": [], "unavailable_languages": []}

        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def reload_config(self) -> None:
        """重新加载配置文件"""
        self.config = self._load_config()
        self._instances.clear()

    def get_strategy(self, language_name: str) -> BaseJudgeClient:
        """
        获取语言对应的判题策略实例

        Args:
            language_name: 语言名称，如 'python3', 'cpp17' 等

        Returns:
            对应的判题策略实例

        Raises:
            ValueError: 如果语言不可用或不存在
        """
        # 检查语言是否存在于注册表中
        if language_name not in STRATEGY_REGISTRY:
            raise ValueError(f"Unknown language: {language_name}")

        # 使用缓存的实例
        if language_name not in self._instances:
            self._instances[language_name] = STRATEGY_REGISTRY[language_name]()

        return self._instances[language_name]

    def get_available_languages(self) -> List[str]:
        """获取所有可用的语言列表"""
        return self.config.get("available_languages", [])

    def get_unavailable_languages(self) -> List[str]:
        """获取所有不可用的语言列表"""
        return self.config.get("unavailable_languages", [])

    def is_language_available(self, language_name: str) -> bool:
        """检查语言是否可用"""
        return language_name in self.config.get("available_languages", [])

    def get_language_config(self, language_name: str) -> Optional[Dict]:
        """获取语言配置"""
        return self.config.get("languages", {}).get(language_name)

    def get_all_strategies(self) -> Dict[str, BaseJudgeClient]:
        """获取所有可用语言的策略实例"""
        strategies = {}
        for lang in self.get_available_languages():
            strategies[lang] = self.get_strategy(lang)
        return strategies

    def create_judge_request(
        self,
        language: str,
        problem_type: str = "normal",
        time_limit: int = 1000,
        memory_limit: int = 256,
        judge_file: Optional[str] = None,
    ) -> JudgeRequest:
        """
        创建判题请求

        Args:
            language: 编程语言
            problem_type: 题目类型 (normal/spj/interactive)
            time_limit: 时间限制（毫秒）
            memory_limit: 内存限制（MB）
            judge_file: Special Judge 或交互程序文件路径

        Returns:
            JudgeRequest 实例
        """
        return JudgeRequest(
            language=language,
            problem_type=problem_type,
            time_limit=time_limit,
            memory_limit=memory_limit,
            judge_file=judge_file,
        )

    def get_compile_commands(
        self, request: JudgeRequest, source_file: str, work_dir: str
    ) -> List[Optional[List[str]]]:
        """
        获取编译命令列表

        根据题目类型返回需要执行的编译命令

        Args:
            request: 判题请求
            source_file: 源代码文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表
        """
        strategy = self.get_strategy(request.language)
        commands = []

        # 编译用户程序
        user_compile = strategy.comp_command(source_file, work_dir)
        if user_compile:
            commands.append(user_compile)

        # Special Judge 或交互题需要编译额外的程序
        if request.problem_type in [ProblemType.SPECIAL_JUDGE, ProblemType.INTERACTIVE]:
            if request.judge_file:
                # 编译 Judge 程序（使用相同的编译器）
                judge_compile = strategy.comp_command(request.judge_file, work_dir)
                if judge_compile:
                    commands.append(judge_compile)

        return commands

    def get_exec_command(
        self, request: JudgeRequest, exec_file: str, work_dir: str
    ) -> List[str]:
        """
        获取执行命令

        根据题目类型返回需要执行的命令

        Args:
            request: 判题请求
            exec_file: 可执行文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表
        """
        strategy = self.get_strategy(request.language)
        return strategy.exec_command(exec_file, work_dir)


# 全局调度器实例
_global_scheduler: Optional[Scheduler] = None


def get_scheduler(config_path: Optional[str] = None) -> Scheduler:
    """
    获取全局调度器实例（单例模式）

    Args:
        config_path: 语言配置文件路径

    Returns:
        调度器实例
    """
    global _global_scheduler

    if _global_scheduler is None:
        _global_scheduler = Scheduler(config_path)

    return _global_scheduler


def reset_scheduler() -> None:
    """重置全局调度器"""
    global _global_scheduler
    _global_scheduler = None
