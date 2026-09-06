# JudgeClient

> Rusin-OJ 判题核心模块

## 架构设计

```
前端(传参) -> 中转站调度 -> 判题文件执行
```

### 前端传参

| 参数 | 类型 | 说明 |
|------|------|------|
| `language` | `str` | 编程语言，如 `cpp17`, `python3` |
| `problem_type` | `str` | 题目类型: `normal`/`spj`/`interactive` |
| `time_limit` | `int` | 时间限制（毫秒） |
| `memory_limit` | `int` | 内存限制（MB） |
| `judge_file` | `str` | Special Judge 或交互程序文件路径（可选） |

### 中转站调度

调度器根据前端参数:
1. 获取对应语言的判题策略实例
2. 组合编译命令（用户程序 + Judge程序）
3. 组合执行命令
4. 返回判题结果

### 判题文件执行

每种语言只负责基础的编译和执行:
- `comp_command()` - 编译源代码
- `exec_command()` - 执行可执行文件

## 目录结构

```
judge/
├── strategies/               # 判题策略
│   ├── base.py              # BaseJudgeClient 基类
│   ├── python.py            # Python 策略
│   ├── java.py              # Java 策略
│   ├── c.py                 # C 策略 (C99/C11/C17/C23 + 优化)
│   ├── cpp98.py             # C++98 策略
│   ├── cpp11.py             # C++11 策略
│   ├── cpp14.py             # C++14 策略
│   ├── cpp17.py             # C++17 策略
│   ├── cpp20.py             # C++20 策略
│   ├── cpp23.py             # C++23 策略
│   ├── csharp.py            # C# 策略
│   ├── rust.py              # Rust 策略
│   └── go.py                # Go 策略
└── dispatcher/               # 中转站模块
    ├── __init__.py          # 模块入口
    ├── detector.py          # 环境检测
    └── scheduler.py         # 语言调度
```

## 接口定义

### BaseJudgeClient

所有判题策略的基类，只定义基础的编译和执行接口。

```python
class BaseJudgeClient(ABC):
    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        """返回执行用户程序的命令"""

    @property
    @abstractmethod
    def extension_name(self) -> str:
        """返回源代码文件扩展名"""

    @property
    @abstractmethod
    def language_name(self) -> str:
        """返回语言名称标识符"""

    @abstractmethod
    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]:
        """返回编译命令，解释型语言返回 None"""
```

### JudgeRequest

判题请求封装。

```python
class JudgeRequest:
    def __init__(
        self,
        language: str,           # 编程语言
        problem_type: str,       # 题目类型 (normal/spj/interactive)
        time_limit: int,         # 时间限制（毫秒）
        memory_limit: int,       # 内存限制（MB）
        judge_file: Optional[str] = None,  # Judge程序路径（可选）
    ): ...
```

### ProblemType

题目类型枚举。

```python
class ProblemType(Enum):
    NORMAL = "normal"           # 普通判题
    SPECIAL_JUDGE = "spj"       # Special Judge
    INTERACTIVE = "interactive" # 交互题
```

### Scheduler

调度器核心方法。

```python
class Scheduler:
    def get_strategy(self, language_name: str) -> BaseJudgeClient:
        """获取语言对应的判题策略实例"""

    def create_judge_request(
        self,
        language: str,
        problem_type: str = "normal",
        time_limit: int = 1000,
        memory_limit: int = 256,
        judge_file: Optional[str] = None,
    ) -> JudgeRequest:
        """创建判题请求"""

    def get_compile_commands(
        self, request: JudgeRequest, source_file: str, work_dir: str
    ) -> List[Optional[List[str]]]:
        """获取编译命令列表"""

    def get_exec_command(
        self, request: JudgeRequest, exec_file: str, work_dir: str
    ) -> List[str]:
        """获取执行命令"""
```

## 使用示例

### 普通判题

```python
from judge.dispatcher import get_scheduler

scheduler = get_scheduler()
strategy = scheduler.get_strategy("cpp17")

# 编译
compile_cmd = strategy.comp_command("main.cpp", "/tmp/work")
# 执行
exec_cmd = strategy.exec_command("/tmp/work/main", "/tmp/work")
```

### Special Judge

```python
from judge.dispatcher import get_scheduler, JudgeRequest

scheduler = get_scheduler()

# 创建判题请求
request = JudgeRequest(
    language="cpp17",
    problem_type="spj",
    time_limit=2000,
    memory_limit=512,
    judge_file="/tmp/spj.cpp"
)

# 获取编译命令（用户程序 + SPJ程序）
compile_cmds = scheduler.get_compile_commands(request, "main.cpp", "/tmp/work")

# 获取执行命令
exec_cmd = scheduler.get_exec_command(request, "/tmp/work/main", "/tmp/work")
```

### 交互题

```python
from judge.dispatcher import get_scheduler, JudgeRequest

scheduler = get_scheduler()

# 创建判题请求
request = JudgeRequest(
    language="cpp17",
    problem_type="interactive",
    time_limit=5000,
    memory_limit=256,
    judge_file="/tmp/interact.cpp"
)

# 获取编译命令（用户程序 + 交互程序）
compile_cmds = scheduler.get_compile_commands(request, "main.cpp", "/tmp/work")

# 获取执行命令
exec_cmd = scheduler.get_exec_command(request, "/tmp/work/main", "/tmp/work")
```

## 支持的语言

| 语言 | 版本 | 优化选项 |
|------|------|----------|
| Python | 3.x | - |
| Java | - | - |
| C | 99/11/17/23 | O1/O2/O3 |
| C++ | 98/11/14/17/20/23 | O1/O2/O3 |
| C# | dotnet/mono | - |
| Rust | - | O1/O2/O3 |
| Go | - | O1/O2/O3 |

## 环境检测

```bash
python -m judge.dispatcher.detector
```

检测结果保存到 `config/languages.json`。
