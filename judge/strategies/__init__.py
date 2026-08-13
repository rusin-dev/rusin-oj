# judge/strategies/__init__.py
from .base import BaseJudgeClient
from .cpp import JudgeClient as CppJudgeClient
from .python import JudgeClient as PythonJudgeClient
from .java import JudgeClient as JavaJudgeClient
from .cppO2 import JudgeClient as CppwithO2JudgeClient

__all__ = [
    "BaseJudgeClient",
    "CppJudgeClient",
    "CppwithO2JudgeClient",
    "JavaJudgeClient",
    "PythonJudgeClient"
]