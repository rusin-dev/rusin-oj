# 贡献指南

感谢你对本 OJ（Online Judge）项目的关注与支持！我们欢迎任何形式的贡献，包括但不限于报告问题、提交代码、完善文档、提出新功能建议等。请花几分钟阅读以下指南，让协作更顺畅。

---

## 行为准则

本项目遵循 [贡献者公约](https://www.contributor-covenant.org/zh-cn/version/2/0/code_of_conduct/)。参与即表示你同意遵守其条款，请共同维护友善、尊重的社区环境。

---

## 如何报告问题

- **检查现有 issue**：在提交前，请搜索已有 issue，避免重复。
- **使用 Issue 模板**：如果项目提供了模板，请按模板填写；否则请清晰描述：
  - 问题现象（包含错误信息、日志等）
  - 复现步骤
  - 预期行为 vs 实际行为
  - 运行环境（操作系统、Python 版本、依赖版本等）
- **安全漏洞**：请通过邮件或私下渠道联系维护者，**不要**公开披露。

---

## 贡献代码

### 1. Fork & 克隆

- Fork 本仓库到你的 GitHub 账号。
- 克隆你的 Fork 到本地：
  ```bash
  git clone https://github.com/你的用户名/项目名.git
  cd 项目名
  ```

### 2. 设置开发环境

推荐使用 **Python 3.8+** 和 **虚拟环境**（venv 或 virtualenv）：

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows
```

安装开发依赖：

```bash
pip install -r requirements-dev.txt   # 若存在开发依赖文件
# 或直接安装项目及测试/代码检查工具
pip install -e .[dev]
```

若项目使用 **Poetry** 或 **Pipenv**，请参照对应命令。

#### 数据库（如有）

- 配置本地数据库（MySQL/PostgreSQL/SQLite）。
- 运行迁移：
  ```bash
  python manage.py migrate      # Django
  # 或 flask db upgrade        # Flask-Migrate
  ```

#### 判题沙箱（如涉及）

判题核心可能依赖 Docker 或特定沙箱环境，请参考项目 README 中“开发环境搭建”部分进行配置。

### 3. 选择任务

- 查看 **issue** 列表，寻找带有 `good first issue` 或 `help wanted` 标签的任务。
- 也可直接提出新功能或改进，先在 issue 中讨论，避免做无用功。

### 4. 创建分支

从 `main`（或 `master`）分支切出新的功能分支：

```bash
git checkout -b feature/简短描述
# 或 fix/修复描述
```

### 5. 编写代码

- **代码风格**：遵循 [PEP 8](https://pep8.org/)。项目可能使用 **Black** 自动格式化，请运行：
  ```bash
  black .
  ```
- **导入排序**：使用 **isort**：
  ```bash
  isort .
  ```
- **静态检查**：使用 **flake8** 或 **pylint** 检查潜在问题。
- **类型标注**：鼓励使用类型提示（Type Hints），并可使用 **mypy** 检查。

### 6. 编写测试

- 新增功能或修复 Bug 都应添加相应的测试用例。
- 测试框架通常为 **pytest**，运行全部测试：
  ```bash
  pytest
  ```
- 确保测试覆盖率不下降（如有覆盖率配置）。

### 7. 编写文档

- 如新增 API 或修改行为，请同步更新 README、文档字符串或项目文档目录。
- 文档字符串建议使用 Google 或 NumPy 风格。

### 8. 提交代码

- **提交信息**遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范，格式：
  ```
  <类型>(<范围>): <简短描述>

  [可选正文]
  [可选脚注]
  ```
  常用类型：`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore` 等。
  示例：
  ```
  feat(judge): 支持 C++20 标准

  添加对 C++20 编译选项的支持，更新判题脚本。
  ```

- 每次提交应保持逻辑独立，避免混合多个不相关的修改。

### 9. 推送 & 创建 Pull Request

- 推送分支到你的 Fork：
  ```bash
  git push origin feature/简短描述
  ```
- 在 GitHub 上打开 Pull Request，目标分支为原仓库的 `main`。
- PR 描述请填写：
  - 关联的 Issue 编号（如 `Closes #123`）
  - 改动概述
  - 测试说明
  - 截图或日志（如适用）

---

## Pull Request 审核流程

- 至少一名维护者将审核你的 PR。
- 可能会要求修改，请及时响应。
- 所有 CI 检查（测试、代码风格、构建）必须通过。
- 合并后，你的贡献将出现在项目历史中，感谢你的付出！

---

## 额外资源

- 项目技术栈文档（如有）
- [GitHub 帮助文档](https://docs.github.com/zh/get-started/quickstart/contributing-to-projects)

---

## 问题或建议

如有任何疑问，欢迎在 issue 中提问，或联系维护者（可在仓库主页找到联系方式）。

再次感谢你的贡献！🎉
