# judge/utils/path_validator.py
"""
路径验证模块 - 防止路径遍历攻击
"""
import os
import re
from pathlib import Path
from typing import Optional


# 危险路径模式
DANGEROUS_PATTERNS = [
    r'\.\.',           # 目录遍历
    r'~',              # 用户主目录
    r'^/',             # 绝对路径 (Unix)
    r'^[A-Za-z]:\\',   # 绝对路径 (Windows)
    r'\x00',           # 空字节
    r'[<>"|?*]',       # 特殊字符
    r'\s',             # 空白字符 (文件名中不应有)
]

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {
    '.py', '.java', '.c', '.cpp', '.rs', '.go', '.cs',
    '.txt', '.in', '.out', '.ans',
}


class PathValidationError(ValueError):
    """路径验证错误"""
    pass


def validate_path(path: str, path_type: str = "file") -> str:
    """
    验证并清理路径，防止路径遍历攻击
    
    Args:
        path: 待验证的路径
        path_type: 路径类型 ("file" 或 "dir")
    
    Returns:
        清理后的安全路径
    
    Raises:
        PathValidationError: 路径验证失败
    """
    if not path or not isinstance(path, str):
        raise PathValidationError("路径不能为空")
    
    # 检查危险模式
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, path):
            raise PathValidationError(f"路径包含危险字符: {path}")
    
    # 规范化路径
    normalized = os.path.normpath(path)
    
    # 再次检查规范化后的路径
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, normalized):
            raise PathValidationError(f"路径包含危险字符: {normalized}")
    
    # 检查是否尝试逃逸当前目录
    if normalized.startswith('..') or os.path.isabs(normalized):
        raise PathValidationError(f"路径尝试逃逸工作目录: {normalized}")
    
    return normalized


def validate_source_file(source_file: str, allowed_extensions: Optional[set] = None) -> str:
    """
    验证源文件路径
    
    Args:
        source_file: 源文件路径
        allowed_extensions: 允许的文件扩展名集合
    
    Returns:
        清理后的源文件路径
    
    Raises:
        PathValidationError: 验证失败
    """
    if allowed_extensions is None:
        allowed_extensions = ALLOWED_EXTENSIONS
    
    # 验证路径
    validated_path = validate_path(source_file, "file")
    
    # 验证文件扩展名
    _, ext = os.path.splitext(validated_path)
    if ext.lower() not in allowed_extensions:
        raise PathValidationError(f"不允许的文件类型: {ext}")
    
    return validated_path


def validate_work_dir(work_dir: str) -> str:
    """
    验证工作目录路径
    
    Args:
        work_dir: 工作目录路径
    
    Returns:
        清理后的工作目录路径
    
    Raises:
        PathValidationError: 验证失败
    """
    # 验证路径
    validated_path = validate_path(work_dir, "dir")
    
    # 确保路径不以文件结尾 (应该是目录)
    if '.' in os.path.basename(validated_path):
        raise PathValidationError(f"工作目录路径不应包含文件扩展名: {validated_path}")
    
    return validated_path


def sanitize_filename(filename: str) -> str:
    """
    清理文件名，移除危险字符
    
    Args:
        filename: 原始文件名
    
    Returns:
        清理后的安全文件名
    """
    # 移除路径分隔符和危险字符
    sanitized = re.sub(r'[/\\<>:"|?*\x00]', '_', filename)
    
    # 移除连续的点 (防止路径遍历)
    sanitized = re.sub(r'\.{2,}', '_', sanitized)
    
    # 移除开头的点 (防止隐藏文件)
    sanitized = re.sub(r'^\.', '_', sanitized)
    
    # 限制长度
    if len(sanitized) > 255:
        name, ext = os.path.splitext(sanitized)
        sanitized = name[:255 - len(ext)] + ext
    
    return sanitized


def validate_file_path(file_path: str, base_dir: Optional[str] = None) -> str:
    """
    验证文件路径是否在允许的目录内
    
    Args:
        file_path: 文件路径
        base_dir: 基准目录 (可选)
    
    Returns:
        清理后的文件路径
    
    Raises:
        PathValidationError: 验证失败
    """
    # 验证路径
    validated_path = validate_path(file_path, "file")
    
    # 如果指定了基准目录，检查是否在目录内
    if base_dir:
        abs_base = os.path.abspath(base_dir)
        abs_file = os.path.abspath(os.path.join(base_dir, validated_path))
        
        if not abs_file.startswith(abs_base):
            raise PathValidationError(f"文件路径逃逸基准目录: {validated_path}")
    
    return validated_path
