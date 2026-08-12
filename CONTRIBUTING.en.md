# Contributing to [rusin-oj]

Thank you for your interest in contributing to this Online Judge (OJ) project! We welcome all forms of contributions, including but not limited to reporting issues, submitting code, improving documentation, and suggesting new features. Please take a few minutes to read through this guide to make collaboration smoother.

---

## Code of Conduct

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you agree to abide by its terms. Please help us maintain a friendly and respectful community.

---

## How to Report Issues

- **Check existing issues**: Before submitting, please search the issue tracker to avoid duplicates.
- **Use the issue template**: If the project provides one, please fill it out; otherwise, clearly describe:
  - The problem (including error messages, logs, etc.)
  - Steps to reproduce
  - Expected vs. actual behavior
  - Environment (OS, Python version, dependency versions, etc.)
- **Security vulnerabilities**: Please contact maintainers via email or private channels – **do not** disclose them publicly.

---

## Contributing Code

### 1. Fork & Clone

- Fork the repository to your GitHub account.
- Clone your fork locally:
  ```bash
  git clone https://github.com/your-username/project-name.git
  cd project-name
  ```

### 2. Set Up Development Environment

We recommend **Python 3.8+** and a **virtual environment** (venv or virtualenv):

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt   # if a dev requirements file exists
# or install the project and test/lint tools directly
pip install -e .[dev]
```

If the project uses **Poetry** or **Pipenv**, please refer to the corresponding commands.

#### Database (if applicable)

- Set up your local database (MySQL/PostgreSQL/SQLite).
- Run migrations:
  ```bash
  python manage.py migrate      # Django
  # or flask db upgrade        # Flask-Migrate
  ```

#### Judging Sandbox (if applicable)

The judging core may depend on Docker or a specific sandbox environment. Please refer to the project README's "Development Setup" section for configuration details.

### 3. Choose a Task

- Check the **issue** list for tasks tagged `good first issue` or `help wanted`.
- You may also propose new features or improvements – please open an issue first to discuss, to avoid wasted effort.

### 4. Create a Branch

Create a new feature branch from `main` (or `master`):

```bash
git checkout -b feature/short-description
# or fix/description
```

### 5. Write Code

- **Code style**: Follow [PEP 8](https://pep8.org/). The project may use **Black** for auto‑formatting; run:
  ```bash
  black .
  ```
- **Import sorting**: Use **isort**:
  ```bash
  isort .
  ```
- **Static checks**: Use **flake8** or **pylint** to catch potential issues.
- **Type hints**: Encouraged; you may run **mypy** for type checking.

### 6. Write Tests

- New features and bug fixes should include corresponding test cases.
- The test framework is typically **pytest** – run all tests:
  ```bash
  pytest
  ```
- Ensure test coverage does not decrease (if coverage is configured).

### 7. Write Documentation

- If you add new APIs or change behavior, please update the README, docstrings, or the project documentation directory accordingly.
- Docstrings should follow Google or NumPy style.

### 8. Commit Your Changes

- **Commit messages** should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
  ```
  <type>(<scope>): <short description>

  [optional body]
  [optional footer]
  ```
  Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, etc.
  Example:
  ```
  feat(judge): add support for C++20

  Add compile options for C++20 and update the judging script.
  ```

- Each commit should be logically independent – avoid mixing unrelated changes.

### 9. Push & Create a Pull Request

- Push your branch to your fork:
  ```bash
  git push origin feature/short-description
  ```
- Open a Pull Request on GitHub, targeting the original repository's `main` branch.
- In the PR description, please include:
  - The related issue number (e.g., `Closes #123`)
  - An overview of changes
  - Testing instructions
  - Screenshots or logs if applicable

---

## Pull Request Review Process

- At least one maintainer will review your PR.
- You may be asked to make changes – please respond promptly.
- All CI checks (tests, code style, build) must pass.
- After merging, your contribution will become part of the project history – thank you!

---

## Additional Resources

- Project tech stack documentation (if available)
- [GitHub Help on Contributing](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

---

## Questions or Suggestions

If you have any questions, feel free to ask in an issue or contact the maintainers (contact information can be found on the repository homepage).

Thank you again for your contribution! 🎉
