# JudgeClient

> Rusin-OJ 判题核心

#### 接口定义

``` python
class BaseJudgeClient(ABC):
    # ...

    @abstractmethod
    def exec_command(self, exec_file: str, work_dir: str) -> List[str]: ...

    @property
    @abstractmethod
    def extension_name(self) -> str: ...

    @property
    @abstractmethod
    def language_name(self) -> str: ...

    @abstractmethod
    def comp_command(self, source_file: str, work_dir: str) -> Optional[List[str]]: ...
```

**说明**

* `exec_command` 执行命令，返回格式为列表
* `extension_name` 扩展名名称，形如 `.py`
* `language_name` 语言名称，形如 `Python`
* `comp_command` 编译命令，如果是解释型语言，返回 `None`

---

*--\*END\*--*
