# judge/strategies/__init__.py
from .base import BaseJudgeClient, SpecialJudgeClient, InteractiveJudgeClient
from .python import JudgeClient as PythonJudgeClient
from .java import JudgeClient as JavaJudgeClient

# C
from .c import (
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
)

# C#
from .csharp import (
    CSharpJudgeClient,
    CSharpMonoJudgeClient,
)

# C++98
from .cpp98 import (
    Cpp98JudgeClient,
    Cpp98O1JudgeClient,
    Cpp98O2JudgeClient,
    Cpp98O3JudgeClient,
)

# C++11
from .cpp11 import (
    Cpp11JudgeClient,
    Cpp11O1JudgeClient,
    Cpp11O2JudgeClient,
    Cpp11O3JudgeClient,
)

# C++14
from .cpp14 import (
    Cpp14JudgeClient,
    Cpp14O1JudgeClient,
    Cpp14O2JudgeClient,
    Cpp14O3JudgeClient,
)

# C++17
from .cpp17 import (
    Cpp17JudgeClient,
    Cpp17O1JudgeClient,
    Cpp17O2JudgeClient,
    Cpp17O3JudgeClient,
)

# C++20
from .cpp20 import (
    Cpp20JudgeClient,
    Cpp20O1JudgeClient,
    Cpp20O2JudgeClient,
    Cpp20O3JudgeClient,
)

# C++23
from .cpp23 import (
    Cpp23JudgeClient,
    Cpp23O1JudgeClient,
    Cpp23O2JudgeClient,
    Cpp23O3JudgeClient,
)

# C++ Special Judge
from .cpp_special import (
    Cpp98SpecialJudgeClient,
    Cpp11SpecialJudgeClient,
    Cpp14SpecialJudgeClient,
    Cpp17SpecialJudgeClient,
    Cpp20SpecialJudgeClient,
    Cpp23SpecialJudgeClient,
)

# C++ Interactive
from .cpp_interactive import (
    Cpp98InteractiveClient,
    Cpp11InteractiveClient,
    Cpp14InteractiveClient,
    Cpp17InteractiveClient,
    Cpp20InteractiveClient,
    Cpp23InteractiveClient,
)

# Rust
from .rust import (
    RustJudgeClient,
    RustO1JudgeClient,
    RustO2JudgeClient,
    RustO3JudgeClient,
)

# Go
from .go import (
    GoJudgeClient,
    GoO1JudgeClient,
    GoO2JudgeClient,
    GoO3JudgeClient,
)

__all__ = [
    # 基类
    "BaseJudgeClient",
    "SpecialJudgeClient",
    "InteractiveJudgeClient",
    # Python
    "PythonJudgeClient",
    # Java
    "JavaJudgeClient",
    # C
    "C99JudgeClient",
    "C99O1JudgeClient",
    "C99O2JudgeClient",
    "C99O3JudgeClient",
    "C11JudgeClient",
    "C11O1JudgeClient",
    "C11O2JudgeClient",
    "C11O3JudgeClient",
    "C17JudgeClient",
    "C17O1JudgeClient",
    "C17O2JudgeClient",
    "C17O3JudgeClient",
    "C23JudgeClient",
    "C23O1JudgeClient",
    "C23O2JudgeClient",
    "C23O3JudgeClient",
    # C#
    "CSharpJudgeClient",
    "CSharpMonoJudgeClient",
    # C++98
    "Cpp98JudgeClient",
    "Cpp98O1JudgeClient",
    "Cpp98O2JudgeClient",
    "Cpp98O3JudgeClient",
    # C++11
    "Cpp11JudgeClient",
    "Cpp11O1JudgeClient",
    "Cpp11O2JudgeClient",
    "Cpp11O3JudgeClient",
    # C++14
    "Cpp14JudgeClient",
    "Cpp14O1JudgeClient",
    "Cpp14O2JudgeClient",
    "Cpp14O3JudgeClient",
    # C++17
    "Cpp17JudgeClient",
    "Cpp17O1JudgeClient",
    "Cpp17O2JudgeClient",
    "Cpp17O3JudgeClient",
    # C++20
    "Cpp20JudgeClient",
    "Cpp20O1JudgeClient",
    "Cpp20O2JudgeClient",
    "Cpp20O3JudgeClient",
    # C++23
    "Cpp23JudgeClient",
    "Cpp23O1JudgeClient",
    "Cpp23O2JudgeClient",
    "Cpp23O3JudgeClient",
    # C++ Special Judge
    "Cpp98SpecialJudgeClient",
    "Cpp11SpecialJudgeClient",
    "Cpp14SpecialJudgeClient",
    "Cpp17SpecialJudgeClient",
    "Cpp20SpecialJudgeClient",
    "Cpp23SpecialJudgeClient",
    # C++ Interactive
    "Cpp98InteractiveClient",
    "Cpp11InteractiveClient",
    "Cpp14InteractiveClient",
    "Cpp17InteractiveClient",
    "Cpp20InteractiveClient",
    "Cpp23InteractiveClient",
    # Rust
    "RustJudgeClient",
    "RustO1JudgeClient",
    "RustO2JudgeClient",
    "RustO3JudgeClient",
    # Go
    "GoJudgeClient",
    "GoO1JudgeClient",
    "GoO2JudgeClient",
    "GoO3JudgeClient",
]