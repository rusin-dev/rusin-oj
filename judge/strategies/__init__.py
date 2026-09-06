# judge/strategies/__init__.py
from .base import BaseJudgeClient, SpecialJudgeClient, InteractiveJudgeClient

# Python
from .python import JudgeClient as PythonJudgeClient
from .python_special import PythonSpecialJudgeClient, PythonInteractiveClient

# Java
from .java import JudgeClient as JavaJudgeClient
from .java_special import JavaSpecialJudgeClient, JavaInteractiveClient

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

# C Special Judge & Interactive
from .c_special import (
    C99SpecialJudgeClient,
    C99InteractiveClient,
    C11SpecialJudgeClient,
    C11InteractiveClient,
    C17SpecialJudgeClient,
    C17InteractiveClient,
    C23SpecialJudgeClient,
    C23InteractiveClient,
)

# C#
from .csharp import (
    CSharpJudgeClient,
    CSharpMonoJudgeClient,
)

# C# Special Judge & Interactive
from .csharp_special import (
    CSharpSpecialJudgeClient,
    CSharpInteractiveClient,
    CSharpMonoSpecialJudgeClient,
    CSharpMonoInteractiveClient,
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

# Rust Special Judge & Interactive
from .rust_special import (
    RustSpecialJudgeClient,
    RustInteractiveClient,
    RustO1SpecialJudgeClient,
    RustO1InteractiveClient,
    RustO2SpecialJudgeClient,
    RustO2InteractiveClient,
    RustO3SpecialJudgeClient,
    RustO3InteractiveClient,
)

# Go
from .go import (
    GoJudgeClient,
    GoO1JudgeClient,
    GoO2JudgeClient,
    GoO3JudgeClient,
)

# Go Special Judge & Interactive
from .go_special import (
    GoSpecialJudgeClient,
    GoInteractiveClient,
    GoO1SpecialJudgeClient,
    GoO1InteractiveClient,
    GoO2SpecialJudgeClient,
    GoO2InteractiveClient,
    GoO3SpecialJudgeClient,
    GoO3InteractiveClient,
)

__all__ = [
    # 基类
    "BaseJudgeClient",
    "SpecialJudgeClient",
    "InteractiveJudgeClient",
    # Python
    "PythonJudgeClient",
    "PythonSpecialJudgeClient",
    "PythonInteractiveClient",
    # Java
    "JavaJudgeClient",
    "JavaSpecialJudgeClient",
    "JavaInteractiveClient",
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
    # C Special Judge & Interactive
    "C99SpecialJudgeClient",
    "C99InteractiveClient",
    "C11SpecialJudgeClient",
    "C11InteractiveClient",
    "C17SpecialJudgeClient",
    "C17InteractiveClient",
    "C23SpecialJudgeClient",
    "C23InteractiveClient",
    # C#
    "CSharpJudgeClient",
    "CSharpMonoJudgeClient",
    # C# Special Judge & Interactive
    "CSharpSpecialJudgeClient",
    "CSharpInteractiveClient",
    "CSharpMonoSpecialJudgeClient",
    "CSharpMonoInteractiveClient",
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
    # Rust Special Judge & Interactive
    "RustSpecialJudgeClient",
    "RustInteractiveClient",
    "RustO1SpecialJudgeClient",
    "RustO1InteractiveClient",
    "RustO2SpecialJudgeClient",
    "RustO2InteractiveClient",
    "RustO3SpecialJudgeClient",
    "RustO3InteractiveClient",
    # Go
    "GoJudgeClient",
    "GoO1JudgeClient",
    "GoO2JudgeClient",
    "GoO3JudgeClient",
    # Go Special Judge & Interactive
    "GoSpecialJudgeClient",
    "GoInteractiveClient",
    "GoO1SpecialJudgeClient",
    "GoO1InteractiveClient",
    "GoO2SpecialJudgeClient",
    "GoO2InteractiveClient",
    "GoO3SpecialJudgeClient",
    "GoO3InteractiveClient",
]