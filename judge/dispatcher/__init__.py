# judge/dispatcher/__init__.py
"""
中转站模块 - 环境检测与语言调度

流程: 前端传参 -> 中转站调度 -> 判题文件执行
"""
from .detector import (
    detect_language,
    detect_all_languages,
    generate_language_config,
    run_detection,
)
from .scheduler import (
    Scheduler,
    JudgeRequest,
    JudgeResult,
    ProblemType,
    get_scheduler,
    reset_scheduler,
    STRATEGY_REGISTRY,
)

__all__ = [
    # 检测功能
    "detect_language",
    "detect_all_languages",
    "generate_language_config",
    "run_detection",
    # 调度功能
    "Scheduler",
    "JudgeRequest",
    "JudgeResult",
    "ProblemType",
    "get_scheduler",
    "reset_scheduler",
    "STRATEGY_REGISTRY",
]
