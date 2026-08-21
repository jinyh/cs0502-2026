"""课程可信实验运行器。

它提供路径、导入、调用、时间和内存限制，但不是抵御恶意本机用户的硬隔离沙箱。
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
import resource
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_ROOTS = ((ROOT / "code" / "examples").resolve(), (ROOT / "code" / "labs").resolve(), (ROOT / "student-work").resolve())
ALLOWED_IMPORTS = {"collections", "heapq", "itertools", "math", "statistics", "sqlite3", "pathlib", "numpy", "pandas", "sklearn", "matplotlib", "networkx"}
BLOCKED_CALLS = {"eval", "exec", "compile", "__import__", "open", "breakpoint"}


def validate_path(raw_path: str) -> Path:
    path = Path(raw_path)
    path = (ROOT / path).resolve() if not path.is_absolute() else path.resolve()
    if path.suffix != ".py" or not path.is_file():
        raise ValueError("只允许运行已存在的 .py 文件")
    if not any(path.is_relative_to(root) for root in ALLOWED_ROOTS):
        raise ValueError("文件必须位于 code/examples、code/labs 或 student-work")
    return path


def validate_source(path: Path) -> None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            modules = [(node.module or "").split(".")[0]]
        else:
            modules = []
        denied = [module for module in modules if module and module not in ALLOWED_IMPORTS]
        if denied:
            raise ValueError(f"不在白名单的导入: {', '.join(sorted(denied))}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
            raise ValueError(f"不允许调用: {node.func.id}")


def limits(memory_mb: int, cpu_seconds: int):
    def apply_limits():
        memory_bytes = memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
        # macOS 拒绝在 preexec_fn 中降低 RLIMIT_DATA/RLIMIT_AS；Linux 可用
        # RLIMIT_AS 做硬上限。macOS 仍有 wall-clock/CPU 限制，内存只能由
        # 外层容器或教学账户配额控制。
        if sys.platform.startswith("linux"):
            resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))

    return apply_limits


def run(path: Path, timeout_seconds: int = 30, memory_mb: int = 512) -> subprocess.CompletedProcess[str]:
    validate_source(path)
    return subprocess.run(
        [sys.executable, "-I", str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
        preexec_fn=limits(memory_mb, timeout_seconds),
        env={"PATH": "/usr/bin:/bin", "MPLBACKEND": "Agg", "PYTHONHASHSEED": "0"},
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="运行课程白名单 Python 实验")
    parser.add_argument("path")
    parser.add_argument("--timeout", type=int, default=30, choices=range(1, 31))
    parser.add_argument("--memory-mb", type=int, default=512, choices=range(64, 513))
    arguments = parser.parse_args()
    try:
        path = validate_path(arguments.path)
        result = run(path, arguments.timeout, arguments.memory_mb)
    except (ValueError, SyntaxError, subprocess.TimeoutExpired) as error:
        print(f"运行被拒绝或终止: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
