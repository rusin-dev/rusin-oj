# judge/dispatcher/scheduler.py
"""
语言调度模块 - 根据语言名称返回对应的判题策略实例
"""
import json
from pathlib import Path
from typing import Dict, Optional, Type

from ..strategies.base import BaseJudgeClient, SpecialJudgeClient, InteractiveJudgeClient
from ..strategies import (
    # Python
    PythonJudgeClient,
    PythonSpecialJudgeClient,
    PythonInteractiveClient,
    # Java
    JavaJudgeClient,
    JavaSpecialJudgeClient,
    JavaInteractiveClient,
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
    # C Special Judge & Interactive
    C99SpecialJudgeClient,
    C99InteractiveClient,
    C11SpecialJudgeClient,
    C11InteractiveClient,
    C17SpecialJudgeClient,
    C17InteractiveClient,
    C23SpecialJudgeClient,
    C23InteractiveClient,
    # C#
    CSharpJudgeClient,
    CSharpMonoJudgeClient,
    # C# Special Judge & Interactive
    CSharpSpecialJudgeClient,
    CSharpInteractiveClient,
    CSharpMonoSpecialJudgeClient,
    CSharpMonoInteractiveClient,
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
    # C++ Special Judge
    Cpp98SpecialJudgeClient,
    Cpp11SpecialJudgeClient,
    Cpp14SpecialJudgeClient,
    Cpp17SpecialJudgeClient,
    Cpp20SpecialJudgeClient,
    Cpp23SpecialJudgeClient,
    # C++ Interactive
    Cpp98InteractiveClient,
    Cpp11InteractiveClient,
    Cpp14InteractiveClient,
    Cpp17InteractiveClient,
    Cpp20InteractiveClient,
    Cpp23InteractiveClient,
    # Rust
    RustJudgeClient,
    RustO1JudgeClient,
    RustO2JudgeClient,
    RustO3JudgeClient,
    # Rust Special Judge & Interactive
    RustSpecialJudgeClient,
    RustInteractiveClient,
    RustO1SpecialJudgeClient,
    RustO1InteractiveClient,
    RustO2SpecialJudgeClient,
    RustO2InteractiveClient,
    RustO3SpecialJudgeClient,
    RustO3InteractiveClient,
    # Go
    GoJudgeClient,
    GoO1JudgeClient,
    GoO2JudgeClient,
    GoO3JudgeClient,
    # Go Special Judge & Interactive
    GoSpecialJudgeClient,
    GoInteractiveClient,
    GoO1SpecialJudgeClient,
    GoO1InteractiveClient,
    GoO2SpecialJudgeClient,
    GoO2InteractiveClient,
    GoO3SpecialJudgeClient,
    GoO3InteractiveClient,
)


# 策略类注册表
STRATEGY_REGISTRY: Dict[str, Type[BaseJudgeClient]] = {
    # Python
    "python3": PythonJudgeClient,
    "python3(spj)": PythonSpecialJudgeClient,
    "python3(interactive)": PythonInteractiveClient,
    # Java
    "java": JavaJudgeClient,
    "java(spj)": JavaSpecialJudgeClient,
    "java(interactive)": JavaInteractiveClient,
    # C
    "c99": C99JudgeClient,
    "c99(with O1)": C99O1JudgeClient,
    "c99(with O2)": C99O2JudgeClient,
    "c99(with O3)": C99O3JudgeClient,
    "c99(spj)": C99SpecialJudgeClient,
    "c99(interactive)": C99InteractiveClient,
    "c11": C11JudgeClient,
    "c11(with O1)": C11O1JudgeClient,
    "c11(with O2)": C11O2JudgeClient,
    "c11(with O3)": C11O3JudgeClient,
    "c11(spj)": C11SpecialJudgeClient,
    "c11(interactive)": C11InteractiveClient,
    "c17": C17JudgeClient,
    "c17(with O1)": C17O1JudgeClient,
    "c17(with O2)": C17O2JudgeClient,
    "c17(with O3)": C17O3JudgeClient,
    "c17(spj)": C17SpecialJudgeClient,
    "c17(interactive)": C17InteractiveClient,
    "c23": C23JudgeClient,
    "c23(with O1)": C23O1JudgeClient,
    "c23(with O2)": C23O2JudgeClient,
    "c23(with O3)": C23O3JudgeClient,
    "c23(spj)": C23SpecialJudgeClient,
    "c23(interactive)": C23InteractiveClient,
    # C#
    "csharp": CSharpJudgeClient,
    "csharp(mono)": CSharpMonoJudgeClient,
    "csharp(spj)": CSharpSpecialJudgeClient,
    "csharp(interactive)": CSharpInteractiveClient,
    "csharp(mono)(spj)": CSharpMonoSpecialJudgeClient,
    "csharp(mono)(interactive)": CSharpMonoInteractiveClient,
    # C++98
    "cpp98": Cpp98JudgeClient,
    "cpp98(with O1)": Cpp98O1JudgeClient,
    "cpp98(with O2)": Cpp98O2JudgeClient,
    "cpp98(with O3)": Cpp98O3JudgeClient,
    "cpp98(spj)": Cpp98SpecialJudgeClient,
    "cpp98(interactive)": Cpp98InteractiveClient,
    # C++11
    "cpp11": Cpp11JudgeClient,
    "cpp11(with O1)": Cpp11O1JudgeClient,
    "cpp11(with O2)": Cpp11O2JudgeClient,
    "cpp11(with O3)": Cpp11O3JudgeClient,
    "cpp11(spj)": Cpp11SpecialJudgeClient,
    "cpp11(interactive)": Cpp11InteractiveClient,
    # C++14
    "cpp14": Cpp14JudgeClient,
    "cpp14(with O1)": Cpp14O1JudgeClient,
    "cpp14(with O2)": Cpp14O2JudgeClient,
    "cpp14(with O3)": Cpp14O3JudgeClient,
    "cpp14(spj)": Cpp14SpecialJudgeClient,
    "cpp14(interactive)": Cpp14InteractiveClient,
    # C++17
    "cpp17": Cpp17JudgeClient,
    "cpp17(with O1)": Cpp17O1JudgeClient,
    "cpp17(with O2)": Cpp17O2JudgeClient,
    "cpp17(with O3)": Cpp17O3JudgeClient,
    "cpp17(spj)": Cpp17SpecialJudgeClient,
    "cpp17(interactive)": Cpp17InteractiveClient,
    # C++20
    "cpp20": Cpp20JudgeClient,
    "cpp20(with O1)": Cpp20O1JudgeClient,
    "cpp20(with O2)": Cpp20O2JudgeClient,
    "cpp20(with O3)": Cpp20O3JudgeClient,
    "cpp20(spj)": Cpp20SpecialJudgeClient,
    "cpp20(interactive)": Cpp20InteractiveClient,
    # C++23
    "cpp23": Cpp23JudgeClient,
    "cpp23(with O1)": Cpp23O1JudgeClient,
    "cpp23(with O2)": Cpp23O2JudgeClient,
    "cpp23(with O3)": Cpp23O3JudgeClient,
    "cpp23(spj)": Cpp23SpecialJudgeClient,
    "cpp23(interactive)": Cpp23InteractiveClient,
    # Rust
    "rust": RustJudgeClient,
    "rust(with O1)": RustO1JudgeClient,
    "rust(with O2)": RustO2JudgeClient,
    "rust(with O3)": RustO3JudgeClient,
    "rust(spj)": RustSpecialJudgeClient,
    "rust(interactive)": RustInteractiveClient,
    "rust(with O1)(spj)": RustO1SpecialJudgeClient,
    "rust(with O1)(interactive)": RustO1InteractiveClient,
    "rust(with O2)(spj)": RustO2SpecialJudgeClient,
    "rust(with O2)(interactive)": RustO2InteractiveClient,
    "rust(with O3)(spj)": RustO3SpecialJudgeClient,
    "rust(with O3)(interactive)": RustO3InteractiveClient,
    # Go
    "go": GoJudgeClient,
    "go(with O1)": GoO1JudgeClient,
    "go(with O2)": GoO2JudgeClient,
    "go(with O3)": GoO3JudgeClient,
    "go(spj)": GoSpecialJudgeClient,
    "go(interactive)": GoInteractiveClient,
    "go(with O1)(spj)": GoO1SpecialJudgeClient,
    "go(with O1)(interactive)": GoO1InteractiveClient,
    "go(with O2)(spj)": GoO2SpecialJudgeClient,
    "go(with O2)(interactive)": GoO2InteractiveClient,
    "go(with O3)(spj)": GoO3SpecialJudgeClient,
    "go(with O3)(interactive)": GoO3InteractiveClient,
}


class Scheduler:
    """
    语言调度器
    负责根据语言名称创建对应的判题策略实例
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
            language_name: 语言名称，如 'python3', 'cpp17(with O2)' 等

        Returns:
            对应的判题策略实例

        Raises:
            ValueError: 如果语言不可用或不存在
        """
        # 检查语言是否存在于配置中
        if language_name not in self.config.get("languages", {}):
            raise ValueError(f"Unknown language: {language_name}")

        # 检查语言是否可用
        lang_config = self.config["languages"][language_name]
        if not lang_config.get("available", False):
            raise ValueError(f"Language is not available: {language_name}")

        # 获取策略类
        if language_name not in STRATEGY_REGISTRY:
            raise ValueError(f"Strategy class not found for: {language_name}")

        # 使用缓存的实例
        if language_name not in self._instances:
            self._instances[language_name] = STRATEGY_REGISTRY[language_name]()

        return self._instances[language_name]

    def get_available_languages(self) -> list:
        """获取所有可用的语言列表"""
        return self.config.get("available_languages", [])

    def get_unavailable_languages(self) -> list:
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
