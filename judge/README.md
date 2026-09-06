# JudgeClient

> Rusin-OJ 判题核心模块

## 概述

判题核心模块负责编译、执行和评判用户提交的代码。支持多种编程语言、Special Judge（特殊判题）和交互题。

## 目录结构

```
judge/
├── strategies/               # 判题策略
│   ├── base.py              # 基类定义
│   ├── python.py            # Python 策略
│   ├── python_special.py    # Python Special Judge/Interactive
│   ├── java.py              # Java 策略
│   ├── java_special.py      # Java Special Judge/Interactive
│   ├── c.py                 # C 策略 (C99/C11/C17/C23)
│   ├── c_special.py         # C Special Judge/Interactive
│   ├── cpp98.py             # C++98 策略
│   ├── cpp11.py             # C++11 策略
│   ├── cpp14.py             # C++14 策略
│   ├── cpp17.py             # C++17 策略
│   ├── cpp20.py             # C++20 策略
│   ├── cpp23.py             # C++23 策略
│   ├── cpp_special.py       # C++ Special Judge
│   ├── cpp_interactive.py   # C++ Interactive
│   ├── csharp.py            # C# 策略
│   ├── csharp_special.py    # C# Special Judge/Interactive
│   ├── rust.py              # Rust 策略
│   ├── rust_special.py      # Rust Special Judge/Interactive
│   ├── go.py                # Go 策略
│   └── go_special.py        # Go Special Judge/Interactive
├── dispatcher/               # 中转站模块
│   ├── __init__.py          # 模块入口
│   ├── detector.py          # 环境检测
│   └── scheduler.py         # 语言调度
└── utils/                    # 工具模块
    ├── __init__.py           # 模块入口
    ├── path_validator.py    # 路径验证（防路径遍历）
    └── resource_limiter.py  # 资源限制（时间/内存/输出）
```

## 资源限制

### 时间限制规则

冗余计算公式: `max_time = time_limit + min(time_limit * 50%, 200ms)`

| 时间限制 | 冗余时间 | 最大运行时间 | 判定结果 |
|----------|----------|--------------|----------|
| 1000ms | min(500,200)=200ms | 1200ms | TLE |
| 100ms | min(50,200)=50ms | 150ms | TLE |
| 10ms | min(5,200)=5ms | 15ms | TLE |
| 500ms | min(250,200)=200ms | 700ms | TLE |

**判定逻辑：**
- 运行时间 ≤ 时间限制：正常判定 (AC/WA等)
- 运行时间 > 时间限制 且 ≤ 最大运行时间：判定 **TLE**，返回实际时间
- 运行时间 > 最大运行时间：**强制终止**，返回最大运行时间

**示例：**
- 时间限制 1000ms，最大运行 1200ms
- 程序运行 800ms 完成 → 正常返回 `Time:800`
- 程序运行 1100ms 完成 → TLE，返回 `Time:1100` + Timeout
- 程序运行 1300ms 未完成 → 强制终止，返回 `Time:1200` + Timeout

### 内存限制规则

| 内存使用 | 判定结果 |
|----------|----------|
| ≤ 限制 | 正常判定 |
| > 限制 | **MLE** |

**说明：**
- 使用峰值内存判定
- 默认提供 8MB 内存冗余，避免临界情况误判
- 例：限制 256MB，实际使用 255MB → AC；使用 257MB → MLE

### 输出限制规则 (OLE)

| 输出大小 | 判定结果 |
|----------|----------|
| ≤ 限制 | 正常判定 |
| > 限制 | **OLE** |

**说明：**
- 默认限制 64KB
- Special Judge 可自定义限制
- 实时监控输出大小，超限立即终止

### 资源限制配置

```python
from judge.utils.resource_limiter import ResourceLimits

# 默认配置
limits = ResourceLimits(
    memory_mb=256.0,           # 内存限制 (MB)
    time_ms=1000.0,            # 时间限制 (ms)
    stack_mb=64.0,             # 栈大小 (MB)
    cpu_time_ms=1000.0,        # CPU时间限制 (ms)
    memory_buffer_mb=8.0,      # 内存冗余 (MB)，默认8MB
    output_limit_kb=64.0,      # 输出限制 (KB)，默认64KB
)

# 时间冗余自动计算: min(time_ms * 50%, 200ms)
limits.time_buffer_ms  # 例: min(500, 200) = 200ms
limits.max_time_ms     # 例: 1000 + 200 = 1200ms
```

## 判定结果

### ExecutionResult 字段

```python
@dataclass
class ExecutionResult:
    stdout: str = ""                # 标准输出
    stderr: str = ""                # 标准错误
    returncode: int = 0             # 返回码
    elapsed_time_ms: float = 0.0    # 实际运行时间 (ms)
    peak_memory_mb: float = 0.0     # 峰值内存 (MB)
    output_size_bytes: int = 0      # 输出大小 (字节)
    
    tle: bool = False               # 时间超限
    mle: bool = False               # 内存超限
    ole: bool = False               # 输出超限
    re: bool = False                # 运行时错误
    
    time_limit_ms: float = 0.0      # 时间限制
    memory_limit_mb: float = 0.0    # 内存限制
    output_limit_kb: float = 64.0   # 输出限制
```

### 返回字典 (to_dict)

```python
result.to_dict()
# {
#     'stdout': '程序输出',
#     'stderr': '',
#     'returncode': 0,
#     'elapsed_time_ms': 123.45,
#     'peak_memory_mb': 12.34,
#     'output_size_bytes': 1024,
#     'tle': False,
#     'mle': False,
#     'ole': False,
#     're': False,
#     'time_limit_ms': 1000.0,
#     'memory_limit_mb': 256.0,
#     'output_limit_kb': 64.0,
#     'time_ratio': 0.1234,
#     'memory_ratio': 0.0482,
#     'is_accepted': True,
# }
```

### 评测结果字符串 (to_judge_string)

```python
# 正常完成
result.to_judge_string()
# "Time:123\nMemory:12.3"

# TLE
result.to_judge_string()
# "Time:1200\nTimeout"

# MLE
result.to_judge_string()
# "Memory:260.0\nMemory Limit Exceeded"

# OLE
result.to_judge_string()
# "Output:65536\nOutput Limit Exceeded"

# RE
result.to_judge_string()
# "Runtime Error\nSegmentation fault"
```

## 使用示例

### 普通判题

```python
from judge.strategies.python import JudgeClient

# 创建客户端
client = JudgeClient()

# 设置自定义资源限制
client.set_resource_limits(
    memory_mb=512.0,
    time_ms=2000.0,
    output_limit_kb=128.0,
)

# 执行代码
result = client.execute_with_limits(
    exec_file="solution.py",
    work_dir="/tmp/judge/123",
    stdin_data="5\n1 2 3 4 5",
)

# 检查结果
if result.is_accepted:
    print(f"AC - Time: {result.elapsed_time_ms:.1f}ms, Memory: {result.peak_memory_mb:.1f}MB")
elif result.tle:
    print(f"TLE - Time: {result.elapsed_time_ms:.1f}ms")
elif result.mle:
    print(f"MLE - Memory: {result.peak_memory_mb:.1f}MB")
elif result.ole:
    print(f"OLE - Output: {result.output_size_bytes} bytes")
elif result.re:
    print(f"RE - {result.stderr}")
```

### Special Judge

```python
from judge.strategies.cpp_special import Cpp17SpecialJudgeClient

# 创建客户端
client = Cpp17SpecialJudgeClient()

# 执行用户程序
user_result = client.execute_with_limits(
    exec_file="/tmp/work/main",
    work_dir="/tmp/work",
    stdin_data="...",
)

# 执行Special Judge
if user_result.is_accepted:
    judge_result = client.execute_judge_with_limits(
        judge_file="/tmp/work/spj",
        input_file="/tmp/work/input.txt",
        output_file="/tmp/work/output.txt",
        work_dir="/tmp/work",
        output_limit_kb=32.0,  # SPJ可自定义输出限制
    )
```

### 交互题

```python
from judge.strategies.cpp_interactive import Cpp17InteractiveClient

# 创建客户端
client = Cpp17InteractiveClient()

# 交互题默认10秒超时
result = client.execute_with_limits(
    exec_file="/tmp/work/main",
    work_dir="/tmp/work",
)
```

## 各语言默认资源限制

| 语言 | 内存限制 | 时间限制 | 栈大小 | 输出限制 |
|------|---------|---------|--------|---------|
| Python3 | 256 MB | 1000 ms | 32 MB | 64 KB |
| Java | 512 MB | 2000 ms | 64 MB | 64 KB |
| C/C++ | 128 MB | 1000 ms | 64 MB | 64 KB |
| Rust | 128 MB | 1000 ms | 64 MB | 64 KB |
| Go | 128 MB | 1000 ms | 64 MB | 64 KB |
| C# (.NET) | 256 MB | 1000 ms | 64 MB | 64 KB |
| C# (Mono) | 192 MB | 1000 ms | 64 KB | 64 KB |
| 交互题 | 256 MB | 10000 ms | 64 KB | 64 KB |

## 平台支持

| 功能 | Linux/macOS | Windows |
|------|-------------|---------|
| 内存监控 | ✅ resource模块 | ✅ psutil |
| 时间监控 | ✅ SIGALRM信号 | ✅ subprocess timeout |
| 系统级限制 | ✅ setrlimit | ❌ 不支持 |
| 进程监控 | ✅ 2ms采样 | ✅ 2ms采样 |

---

## 接口定义

### BaseJudgeClient

所有判题策略的基类，定义了判题所需的基本接口。

```python
class BaseJudgeClient(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._resource_limits: Optional[ResourceLimits] = None

    @property
    def default_resource_limits(self) -> ResourceLimits:
        """返回默认资源限制"""
        return DEFAULT_LIMITS
    
    def set_resource_limits(
        self,
        memory_mb: Optional[float] = None,
        time_ms: Optional[float] = None,
        stack_mb: Optional[float] = None,
        cpu_time_ms: Optional[float] = None,
        memory_buffer_mb: Optional[float] = None,
        time_buffer_ratio: Optional[float] = None,
        output_limit_kb: Optional[float] = None,
    ) -> None:
        """设置资源限制"""

    def get_resource_limits(self) -> ResourceLimits:
        """获取当前资源限制"""

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
        """返回编译源代码的命令"""
    
    def execute_with_limits(
        self,
        exec_file: str,
        work_dir: str,
        stdin_data: Optional[str] = None,
        output_limit_kb: Optional[float] = None,
    ) -> ExecutionResult:
        """执行命令并应用资源限制"""
```

#### 方法说明

| 方法 | 类型 | 说明 |
|------|------|------|
| `exec_command()` | 抽象方法 | 返回执行用户程序的命令列表 |
| `extension_name` | 抽象属性 | 返回源代码文件扩展名 |
| `language_name` | 抽象属性 | 返回语言名称标识符 |
| `comp_command()` | 抽象方法 | 返回编译命令，解释型语言返回 `None` |
| `set_resource_limits()` | 普通方法 | 设置资源限制 |
| `get_resource_limits()` | 普通方法 | 获取当前资源限制 |
| `execute_with_limits()` | 普通方法 | 执行代码并应用限制，返回ExecutionResult |

---

### SpecialJudgeClient

Special Judge（特殊判题）基类，继承自 `BaseJudgeClient`，用于答案不唯一或需要特殊验证的题目。

```python
class SpecialJudgeClient(BaseJudgeClient):
    @abstractmethod
    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        """返回执行 Special Judge 程序的命令"""

    @abstractmethod
    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        """返回编译 Special Judge 程序的命令"""

    @property
    def judge_extension(self) -> str:
        """返回 Special Judge 程序的文件扩展名"""
    
    def execute_judge_with_limits(
        self,
        judge_file: str,
        input_file: str,
        output_file: str,
        work_dir: str,
        output_limit_kb: Optional[float] = None,
    ) -> ExecutionResult:
        """执行Special Judge并应用资源限制"""
```

---

### InteractiveJudgeClient

交互题判题基类，继承自 `BaseJudgeClient`，用于需要与评测程序进行交互的题目。

```python
class InteractiveJudgeClient(BaseJudgeClient):
    @abstractmethod
    def interactive_exec_command(
        self, exec_file: str, interact_file: str, work_dir: str
    ) -> List[str]:
        """返回交互题执行命令"""

    @abstractmethod
    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        """返回编译交互评测程序的命令"""

    @property
    def interact_extension(self) -> str:
        """返回交互评测程序的文件扩展名"""

    @property
    def default_timeout(self) -> int:
        """返回默认超时时间（秒），默认10秒"""
```

---

## 环境检测

运行以下命令检测可用的编译器/解释器：

```bash
python -m judge.dispatcher.detector
```

检测结果会保存到 `config/languages.json`。

## 语言调度

```python
from judge.dispatcher import get_scheduler

# 获取调度器实例
scheduler = get_scheduler()

# 获取可用语言列表
available = scheduler.get_available_languages()

# 获取语言策略
strategy = scheduler.get_strategy("cpp17")

# 检查语言是否可用
is_available = scheduler.is_language_available("cpp17")
```

## 添加新语言

1. 在 `judge/strategies/` 下创建新的策略文件
2. 继承 `BaseJudgeClient`、`SpecialJudgeClient` 或 `InteractiveJudgeClient`
3. 实现必要的抽象方法
4. 在 `judge/strategies/__init__.py` 中导出
5. 在 `judge/dispatcher/scheduler.py` 中注册
6. 在 `judge/dispatcher/detector.py` 中添加检测配置
