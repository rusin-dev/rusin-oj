# judge/dispatcher/detector.py
"""
环境检测模块 - 检测可用的编译器/解释器并保存到 JSON 配置文件
"""
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional


# 语言检测配置
# 每种语言定义: 命令、版本参数、版本解析函数、依赖的策略类
LANGUAGE_DETECTORS: Dict[str, Dict] = {
    "python3": {
        "command": "python3",
        "version_args": ["--version"],
        "strategy_class": "PythonJudgeClient",
    },
    "java": {
        "command": "javac",
        "version_args": ["-version"],
        "strategy_class": "JavaJudgeClient",
    },
    # C++ 各版本使用相同的 g++ 编译器
    "cpp98": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp98JudgeClient",
        "std_flag": "-std=c++98",
    },
    "cpp11": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp11JudgeClient",
        "std_flag": "-std=c++11",
    },
    "cpp14": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp14JudgeClient",
        "std_flag": "-std=c++14",
    },
    "cpp17": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp17JudgeClient",
        "std_flag": "-std=c++17",
    },
    "cpp20": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp20JudgeClient",
        "std_flag": "-std=c++20",
    },
    "cpp23": {
        "command": "g++",
        "version_args": ["--version"],
        "strategy_class": "Cpp23JudgeClient",
        "std_flag": "-std=c++23",
    },
    "rust": {
        "command": "rustc",
        "version_args": ["--version"],
        "strategy_class": "RustJudgeClient",
    },
    "go": {
        "command": "go",
        "version_args": ["version"],
        "strategy_class": "GoJudgeClient",
    },
}

# 优化级别
OPT_LEVELS = ["", "O1", "O2", "O3"]

# 优化级别到策略类后缀的映射
OPT_SUFFIX_MAP = {
    "": "",
    "O1": "O1",
    "O2": "O2",
    "O3": "O3",
}


def _run_command(command: str, args: List[str], timeout: int = 5) -> tuple[bool, str]:
    """
    执行命令并返回是否成功及输出
    """
    try:
        creation_flags = 0
        if os.name == "nt":
            creation_flags = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(
            [command] + args,
            capture_output=True,
            text=True,
            timeout=timeout,
            creationflags=creation_flags,
        )
        output = result.stdout + result.stderr
        return result.returncode == 0, output.strip()
    except FileNotFoundError:
        return False, f"Command not found: {command}"
    except subprocess.TimeoutExpired:
        return False, f"Command timed out: {command}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def _extract_version(output: str, command: str) -> Optional[str]:
    """
    从命令输出中提取版本号
    """
    if not output:
        return None

    lines = output.split("\n")
    for line in lines:
        line = line.strip()
        # 尝试常见的版本号模式
        # Python: Python 3.11.0
        # G++: g++ (Ubuntu 11.3.0) 11.3.0
        # Rust: rustc 1.75.0
        # Go: go version go1.21.5 linux/amd64
        if any(
            keyword in line.lower()
            for keyword in ["python", "g++", "gcc", "rustc", "go version", "javac"]
        ):
            return line
        # 尝试提取版本号
        parts = line.split()
        for part in parts:
            if any(c.isdigit() for c in part):
                return part
    return lines[0] if lines else None


def detect_language(language_name: str) -> Dict:
    """
    检测单个语言是否可用
    """
    if language_name not in LANGUAGE_DETECTORS:
        return {
            "available": False,
            "error": f"Unknown language: {language_name}",
        }

    config = LANGUAGE_DETECTORS[language_name]
    command = config["command"]
    version_args = config["version_args"]

    success, output = _run_command(command, version_args)

    if success:
        version = _extract_version(output, command)
        return {
            "available": True,
            "command": command,
            "version": version,
            "strategy_class": config["strategy_class"],
            "std_flag": config.get("std_flag"),
        }
    else:
        return {
            "available": False,
            "command": command,
            "error": output,
        }


def detect_all_languages() -> Dict[str, Dict]:
    """
    检测所有语言的可用性
    """
    results = {}

    for language_name in LANGUAGE_DETECTORS:
        results[language_name] = detect_language(language_name)

    return results


def generate_language_config(
    detection_results: Dict[str, Dict],
    output_path: Optional[str] = None,
) -> Dict:
    """
    根据检测结果生成语言配置
    包含所有可能的语言+优化级别组合
    """
    if output_path is None:
        # 默认路径: 项目根目录/config/languages.json
        project_root = Path(__file__).parent.parent.parent
        output_path = project_root / "config" / "languages.json"

    config = {
        "languages": {},
        "available_languages": [],
        "unavailable_languages": [],
    }

    # 遍历所有语言
    for language_name, detection in detection_results.items():
        # 如果是 C++ 系列，需要为每个优化级别创建配置
        if language_name.startswith("cpp"):
            for opt_level in OPT_LEVELS:
                if opt_level:
                    full_name = f"{language_name}(with {opt_level})"
                    strategy_suffix = OPT_SUFFIX_MAP[opt_level]
                else:
                    full_name = language_name
                    strategy_suffix = ""

                # 构造策略类名
                base_class = detection.get("strategy_class", "")
                if strategy_suffix:
                    strategy_class = f"Cpp{language_name[3:]}{strategy_suffix}JudgeClient"
                else:
                    strategy_class = base_class

                available = detection.get("available", False)
                lang_config = {
                    "name": full_name,
                    "extension": ".cpp",
                    "strategy_class": strategy_class,
                    "available": available,
                    "std_flag": detection.get("std_flag"),
                }

                config["languages"][full_name] = lang_config

                if available:
                    config["available_languages"].append(full_name)
                else:
                    config["unavailable_languages"].append(full_name)

        # Rust 系列
        elif language_name == "rust":
            for opt_level in OPT_LEVELS:
                if opt_level:
                    full_name = f"rust(with {opt_level})"
                    strategy_suffix = OPT_SUFFIX_MAP[opt_level]
                else:
                    full_name = "rust"
                    strategy_suffix = ""

                if strategy_suffix:
                    strategy_class = f"Rust{strategy_suffix}JudgeClient"
                else:
                    strategy_class = "RustJudgeClient"

                available = detection.get("available", False)
                lang_config = {
                    "name": full_name,
                    "extension": ".rs",
                    "strategy_class": strategy_class,
                    "available": available,
                }

                config["languages"][full_name] = lang_config

                if available:
                    config["available_languages"].append(full_name)
                else:
                    config["unavailable_languages"].append(full_name)

        # Go 系列
        elif language_name == "go":
            for opt_level in OPT_LEVELS:
                if opt_level:
                    full_name = f"go(with {opt_level})"
                    strategy_suffix = OPT_SUFFIX_MAP[opt_level]
                else:
                    full_name = "go"
                    strategy_suffix = ""

                if strategy_suffix:
                    strategy_class = f"Go{strategy_suffix}JudgeClient"
                else:
                    strategy_class = "GoJudgeClient"

                available = detection.get("available", False)
                lang_config = {
                    "name": full_name,
                    "extension": ".go",
                    "strategy_class": strategy_class,
                    "available": available,
                }

                config["languages"][full_name] = lang_config

                if available:
                    config["available_languages"].append(full_name)
                else:
                    config["unavailable_languages"].append(full_name)

        # Python 和 Java
        else:
            available = detection.get("available", False)
            extension = ".py" if language_name == "python3" else ".java"
            lang_config = {
                "name": language_name,
                "extension": extension,
                "strategy_class": detection.get("strategy_class", ""),
                "available": available,
            }

            config["languages"][language_name] = lang_config

            if available:
                config["available_languages"].append(language_name)
            else:
                config["unavailable_languages"].append(language_name)

    # 保存到 JSON 文件
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    return config


def run_detection(output_path: Optional[str] = None) -> Dict:
    """
    运行完整的环境检测流程
    1. 检测所有语言
    2. 生成配置文件
    3. 返回配置
    """
    print("Starting language environment detection...")

    # 检测所有语言
    results = detect_all_languages()

    # 打印检测结果
    for lang, result in results.items():
        status = "[OK]" if result.get("available") else "[FAIL]"
        print(f"  {status} {lang}: {result.get('version', result.get('error', 'Unknown'))}")

    # 生成配置
    config = generate_language_config(results, output_path)

    print(f"\nDetection complete!")
    print(f"  Available languages: {len(config['available_languages'])}")
    print(f"  Unavailable languages: {len(config['unavailable_languages'])}")
    print(f"  Config saved to: {output_path or 'config/languages.json'}")

    return config


if __name__ == "__main__":
    run_detection()
