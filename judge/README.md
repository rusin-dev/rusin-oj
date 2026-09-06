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
└── dispatcher/               # 中转站模块
    ├── __init__.py          # 模块入口
    ├── detector.py          # 环境检测
    └── scheduler.py         # 语言调度
```

## 接口定义

### BaseJudgeClient

所有判题策略的基类，定义了判题所需的基本接口。

```python
class BaseJudgeClient(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]:
        """
        返回执行用户程序的命令

        Args:
            exec_file: 可执行文件的完整路径
            work_dir: 工作目录路径

        Returns:
            执行命令列表，例如: ['./main', 'arg1', 'arg2']

        Example:
            # Python
            return ['python3', exec_file]

            # C++ (编译后直接执行)
            return [exec_file]

            # Java
            return ['java', '-cp', work_dir, 'Main']
        """

    @property
    @abstractmethod
    def extension_name(self) -> str:
        """
        返回源代码文件扩展名

        Returns:
            文件扩展名，例如: '.py', '.cpp', '.java'

        Example:
            return '.cpp'
        """

    @property
    @abstractmethod
    def language_name(self) -> str:
        """
        返回语言名称标识符

        Returns:
            语言名称，例如: 'python3', 'cpp17', 'java'

        Example:
            return 'cpp17'
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

        Example:
            # C++ 编译
            return [
                'g++', source_file, '-o', f"{work_dir}/main",
                '-std=c++17', '-DONLINE_JUDGE', '-Wall'
            ]

            # Python (无需编译)
            return None
        """
```

#### 方法说明

| 方法 | 类型 | 说明 |
|------|------|------|
| `exec_command()` | 抽象方法 | 返回执行用户程序的命令列表 |
| `extension_name` | 抽象属性 | 返回源代码文件扩展名 |
| `language_name` | 抽象属性 | 返回语言名称标识符 |
| `comp_command()` | 抽象方法 | 返回编译命令，解释型语言返回 `None` |

#### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `exec_file` | `str` | 可执行文件的完整路径 |
| `work_dir` | `str` | 工作目录路径 |
| `source_file` | `str` | 源代码文件的完整路径 |

#### 返回值说明

| 返回值 | 类型 | 说明 |
|--------|------|------|
| 执行命令 | `List[str]` | 命令及其参数组成的列表 |
| 编译命令 | `Optional[List[str]]` | 编译命令列表或 `None` |

---

### SpecialJudgeClient

Special Judge（特殊判题）基类，继承自 `BaseJudgeClient`，用于答案不唯一或需要特殊验证的题目。

```python
class SpecialJudgeClient(BaseJudgeClient):
    @abstractmethod
    def judge_command(
        self, judge_file: str, input_file: str, output_file: str, work_dir: str
    ) -> List[str]:
        """
        返回执行 Special Judge 程序的命令

        Args:
            judge_file: Special Judge 程序文件路径
            input_file: 题目输入文件路径
            output_file: 用户程序输出文件路径
            work_dir: 工作目录

        Returns:
            执行命令列表

        Example:
            return [f"{work_dir}/spj", input_file, output_file]
        """

    @abstractmethod
    def comp_judge_command(self, judge_file: str, work_dir: str) -> Optional[List[str]]:
        """
        返回编译 Special Judge 程序的命令

        Args:
            judge_file: Special Judge 源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None

        Example:
            return [
                'g++', judge_file, '-o', f"{work_dir}/spj",
                '-std=c++17', '-Wall'
            ]
        """

    @property
    def judge_extension(self) -> str:
        """
        返回 Special Judge 程序的文件扩展名

        Returns:
            文件扩展名，默认与主程序相同

        Example:
            return self.extension_name  # 默认返回主程序扩展名
        """
```

#### 方法说明

| 方法 | 类型 | 说明 |
|------|------|------|
| `judge_command()` | 抽象方法 | 返回执行 Special Judge 程序的命令列表 |
| `comp_judge_command()` | 抽象方法 | 返回编译 Special Judge 程序的命令 |
| `judge_extension` | 属性 | 返回 Special Judge 程序的文件扩展名 |

#### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `judge_file` | `str` | Special Judge 程序文件路径 |
| `input_file` | `str` | 题目输入文件路径 |
| `output_file` | `str` | 用户程序输出文件路径 |
| `work_dir` | `str` | 工作目录路径 |

#### 返回值说明

| 返回值 | 类型 | 说明 |
|--------|------|------|
| 执行命令 | `List[str]` | Special Judge 执行命令列表 |
| 编译命令 | `Optional[List[str]]` | 编译命令列表或 `None` |

---

### InteractiveJudgeClient

交互题判题基类，继承自 `BaseJudgeClient`，用于需要与评测程序进行交互的题目。

```python
class InteractiveJudgeClient(BaseJudgeClient):
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

        Example:
            return [f"{work_dir}/interact"]
        """

    @abstractmethod
    def comp_interact_command(
        self, interact_file: str, work_dir: str
    ) -> Optional[List[str]]:
        """
        返回编译交互评测程序的命令

        Args:
            interact_file: 交互评测程序源文件路径
            work_dir: 工作目录

        Returns:
            编译命令列表，如果无需编译返回 None

        Example:
            return [
                'g++', interact_file, '-o', f"{work_dir}/interact",
                '-std=c++17', '-Wall'
            ]
        """

    @property
    def interact_extension(self) -> str:
        """
        返回交互评测程序的文件扩展名

        Returns:
            文件扩展名，默认与主程序相同
        """

    @property
    def default_timeout(self) -> int:
        """
        返回默认超时时间（秒）

        Returns:
            超时时间，默认为 10 秒
        """
```

#### 方法说明

| 方法 | 类型 | 说明 |
|------|------|------|
| `interactive_exec_command()` | 抽象方法 | 返回交互题执行命令列表 |
| `comp_interact_command()` | 抽象方法 | 返回编译交互评测程序的命令 |
| `interact_extension` | 属性 | 返回交互评测程序的文件扩展名 |
| `default_timeout` | 属性 | 返回默认超时时间（秒） |

#### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| `exec_file` | `str` | 用户程序可执行文件路径 |
| `interact_file` | `str` | 交互评测程序文件路径 |
| `work_dir` | `str` | 工作目录路径 |

#### 返回值说明

| 返回值 | 类型 | 说明 |
|--------|------|------|
| 执行命令 | `List[str]` | 交互题执行命令列表 |
| 编译命令 | `Optional[List[str]]` | 编译命令列表或 `None` |

## 判题类型

### 普通判题

直接执行用户程序，与标准输入输出进行交互。

```python
# 示例：C++17 普通判题
strategy = scheduler.get_strategy("cpp17")
compile_cmd = strategy.comp_command("main.cpp", "/tmp/work")
exec_cmd = strategy.exec_command("/tmp/work/main", "/tmp/work")
```

### Special Judge

使用自定义的判题程序来验证答案，适用于：
- 答案不唯一的问题
- 需要浮点数比较的问题
- 需要特殊格式验证的问题

```python
# 示例：C++17 Special Judge
strategy = scheduler.get_strategy("cpp17(spj)")
compile_cmd = strategy.comp_command("main.cpp", "/tmp/work")
judge_cmd = strategy.judge_command("/tmp/work/spj", "input.txt", "output.txt", "/tmp/work")
```

### 交互题

程序需要与评测程序进行交互，通常：
- 通过标准输入输出与评测程序通信
- 需要在特定时间结束程序
- 需要处理管道通信

```python
# 示例：C++17 交互题
strategy = scheduler.get_strategy("cpp17(interactive)")
compile_cmd = strategy.comp_command("main.cpp", "/tmp/work")
interact_cmd = strategy.interactive_exec_command("/tmp/work/main", "/tmp/work/interact", "/tmp/work")
```

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
