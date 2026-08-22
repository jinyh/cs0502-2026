"""课程可信实验运行器。

它提供路径、导入、调用、时间和内存限制，并负责初始化与测试 Lab。
它不是抵御恶意本机用户的硬隔离沙箱。
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
import re
import resource
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_ROOT = (ROOT / "code" / "examples").resolve()
LABS_ROOT = (ROOT / "code" / "labs").resolve()
STUDENT_WORK_ROOT = (ROOT / "student-work").resolve()
STUDENT_LABS_ROOT = STUDENT_WORK_ROOT / "labs"
ALLOWED_ROOTS = (EXAMPLES_ROOT, LABS_ROOT, STUDENT_WORK_ROOT)
ALLOWED_IMPORTS = {"collections", "heapq", "itertools", "math", "statistics", "sqlite3", "pathlib", "numpy", "pandas", "sklearn", "matplotlib", "networkx"}
BLOCKED_CALLS = {"eval", "exec", "compile", "__import__", "open", "breakpoint"}
MAX_OUTPUT_CHARS = 64 * 1024


def display_path(path: Path):
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


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


def sandbox_environment():
    return {
        "PATH": "/usr/bin:/bin",
        "MPLBACKEND": "Agg",
        "PYTHONHASHSEED": "0",
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
    }


def run_process(command, cwd: Path, timeout_seconds: int, memory_mb: int):
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
        preexec_fn=limits(memory_mb, timeout_seconds),
        env=sandbox_environment(),
    )


def run(path: Path, timeout_seconds: int = 30, memory_mb: int = 512) -> subprocess.CompletedProcess[str]:
    validate_source(path)
    return run_process(
        [sys.executable, "-I", str(path)],
        ROOT,
        timeout_seconds,
        memory_mb,
    )


def lab_directory(lab_id: str) -> Path:
    if not re.fullmatch(r"lab-\d{2}-[a-z0-9-]+", lab_id):
        raise ValueError("Lab 编号格式无效")
    lab = (LABS_ROOT / lab_id).resolve()
    if not lab.is_relative_to(LABS_ROOT) or not lab.is_dir():
        raise ValueError(f"不存在的 Lab: {lab_id}")
    return lab


def student_solution(lab_id: str) -> Path:
    return STUDENT_LABS_ROOT / lab_id / "solution.py"


def initialize_lab(lab_id: str) -> Path:
    lab = lab_directory(lab_id)
    source = lab / "starter.py"
    if not source.is_file():
        raise ValueError(f"Lab 缺少 starter: {lab_id}")
    destination = student_solution(lab_id)
    if destination.exists():
        raise ValueError(f"学生副本已存在，不覆盖: {display_path(destination)}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    return destination


def test_lab(lab_id: str, timeout_seconds: int = 30, memory_mb: int = 512):
    lab = lab_directory(lab_id)
    solution = student_solution(lab_id)
    if not solution.is_file():
        raise ValueError(f"尚未初始化学生副本: {display_path(solution)}")
    validate_path(str(solution))
    validate_source(solution)

    official_test = lab / "test_lab.py"
    if not official_test.is_file():
        raise ValueError(f"Lab 缺少公开测试: {lab_id}")

    with tempfile.TemporaryDirectory(prefix=f"cs0502-{lab_id}-") as temp_dir:
        temp_root = Path(temp_dir)
        shutil.copyfile(solution, temp_root / "starter.py")
        shutil.copyfile(official_test, temp_root / "test_lab.py")
        return run_process(
            [sys.executable, "-I", "-m", "pytest", "-q", str(temp_root / "test_lab.py")],
            temp_root,
            timeout_seconds,
            memory_mb,
        )


def truncate_output(text: str) -> str:
    if len(text) <= MAX_OUTPUT_CHARS:
        return text
    omitted = len(text) - MAX_OUTPUT_CHARS
    return f"{text[:MAX_OUTPUT_CHARS]}\n... 输出已截断，省略 {omitted} 个字符 ...\n"


def add_limits(parser):
    parser.add_argument("--timeout", type=int, default=30, choices=range(1, 31))
    parser.add_argument("--memory-mb", type=int, default=512, choices=range(64, 513))


def argument_parser():
    parser = argparse.ArgumentParser(description="运行课程白名单 Python 示例与实验")
    commands = parser.add_subparsers(dest="command", required=True)

    run_parser = commands.add_parser("run", help="运行允许目录中的 Python 文件")
    run_parser.add_argument("path")
    add_limits(run_parser)

    lab_parser = commands.add_parser("lab", help="初始化或测试核心 Lab")
    lab_commands = lab_parser.add_subparsers(dest="lab_command", required=True)
    init_parser = lab_commands.add_parser("init", help="复制只读 starter 到 student-work")
    init_parser.add_argument("lab_id")
    test_parser = lab_commands.add_parser("test", help="用官方公开测试检查学生副本")
    test_parser.add_argument("lab_id")
    add_limits(test_parser)
    return parser


def main(argv=None) -> int:
    raw_arguments = list(sys.argv[1:] if argv is None else argv)
    # 兼容旧入口：runner.py <path> 等价于 runner.py run <path>。
    if raw_arguments and raw_arguments[0] not in {"run", "lab"}:
        raw_arguments.insert(0, "run")
    arguments = argument_parser().parse_args(raw_arguments)
    try:
        if arguments.command == "run":
            path = validate_path(arguments.path)
            result = run(path, arguments.timeout, arguments.memory_mb)
        elif arguments.lab_command == "init":
            destination = initialize_lab(arguments.lab_id)
            print(f"已创建学生副本: {display_path(destination)}")
            return 0
        else:
            result = test_lab(arguments.lab_id, arguments.timeout, arguments.memory_mb)
    except (ValueError, SyntaxError, subprocess.TimeoutExpired) as error:
        print(f"运行被拒绝或终止: {error}", file=sys.stderr)
        return 2
    sys.stdout.write(truncate_output(result.stdout))
    sys.stderr.write(truncate_output(result.stderr))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
