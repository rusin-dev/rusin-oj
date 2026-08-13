FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 安装 uv 包管理器
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 先复制依赖清单，利用 Docker 层缓存
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# 复制项目源码
COPY . .

# 将虚拟环境加入 PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5000

CMD ["python", "main.py"]
