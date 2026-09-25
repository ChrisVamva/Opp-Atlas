import os
import subprocess
from pathlib import Path

SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", "venv", ".venv",
    "env", ".env", "dist", "build", ".next", ".nuxt",
    "coverage", ".pytest_cache", ".mypy_cache", ".ruff_cache"
}

KEY_FILES = {
    "README.md", "README.txt", "requirements.txt", "package.json",
    "pyproject.toml", "setup.py", "Dockerfile", "docker-compose.yml",
    "main.py", "app.py", "index.js", "index.ts", "manage.py",
    "config.py", "settings.py", ".env.example", "tsconfig.json"
}


def scan_project(root_dir: str, max_files: int = 100) -> dict:
    root = Path(root_dir).resolve()
    file_tree = []
    key_contents = {}
    file_count = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        depth = len(Path(dirpath).relative_to(root).parts)
        if depth > 5:
            continue
        for filename in filenames:
            if file_count >= max_files:
                break
            file_path = Path(dirpath) / filename
            rel_path = str(file_path.relative_to(root))
            file_tree.append(rel_path)
            file_count += 1
            if filename in KEY_FILES:
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                    key_contents[rel_path] = content[:3000]
                except Exception:
                    pass

    return {"root": str(root), "file_tree": file_tree, "key_files": key_contents, "total_files": file_count}


def format_project_summary(scan: dict) -> str:
    lines = [
        f"Project root: {scan['root']}",
        f"Total files: {scan['total_files']}",
        "",
        "File tree:",
    ]
    for f in scan["file_tree"][:60]:
        lines.append(f"  {f}")
    if scan["total_files"] > 60:
        lines.append(f"  ... and {scan['total_files'] - 60} more files")
    if scan["key_files"]:
        lines.append("\nKey file contents:")
        for path, content in scan["key_files"].items():
            lines.append(f"\n--- {path} ---")
            lines.append(content)
    return "\n".join(lines)


def _resolve(path: str, project_root: str) -> Path:
    p = Path(path)
    if project_root and not p.is_absolute():
        p = Path(project_root) / p
    return p


def read_file(path: str, project_root: str = None) -> str:
    try:
        return _resolve(path, project_root).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR reading {path}: {e}"


def write_file(path: str, content: str, project_root: str = None) -> str:
    try:
        p = _resolve(path, project_root)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        return f"OK: wrote {len(content)} chars to {p}"
    except Exception as e:
        return f"ERROR writing {path}: {e}"


def patch_file(path: str, old_content: str, new_content: str, project_root: str = None) -> str:
    try:
        p = _resolve(path, project_root)
        text = p.read_text(encoding="utf-8", errors="ignore")
        if old_content not in text:
            return f"ERROR: target text not found in {p} — file may have changed"
        p.write_text(text.replace(old_content, new_content, 1), encoding="utf-8")
        return f"OK: patched {p}"
    except Exception as e:
        return f"ERROR patching {path}: {e}"


def append_file(path: str, content: str, project_root: str = None) -> str:
    try:
        p = _resolve(path, project_root)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "a", encoding="utf-8") as f:
            f.write(content)
        return f"OK: appended {len(content)} chars to {p}"
    except Exception as e:
        return f"ERROR appending {path}: {e}"


def run_command(command: str, cwd: str = None) -> dict:
    try:
        result = subprocess.run(
            command, shell=True, cwd=cwd,
            capture_output=True, text=True, timeout=120
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout[:4000],
            "stderr": result.stderr[:2000],
            "success": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": "Timed out after 120s", "success": False}
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e), "success": False}


def search_code(pattern: str, root_dir: str, file_extension: str = None) -> list:
    results = []
    root = Path(root_dir).resolve()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if file_extension and not filename.endswith(file_extension):
                continue
            file_path = Path(dirpath) / filename
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                if pattern.lower() in content.lower():
                    lines = content.split("\n")
                    matches = [(i + 1, line.strip()) for i, line in enumerate(lines)
                               if pattern.lower() in line.lower()]
                    results.append({
                        "file": str(file_path.relative_to(root)),
                        "matches": matches[:5],
                    })
            except Exception:
                pass
            if len(results) >= 20:
                return results
    return results


def list_directory(path: str, project_root: str = None) -> list:
    try:
        p = _resolve(path, project_root)
        return [
            {"name": item.name, "type": "dir" if item.is_dir() else "file",
             "size": item.stat().st_size if item.is_file() else None}
            for item in sorted(p.iterdir())
            if item.name not in SKIP_DIRS
        ]
    except Exception as e:
        return [{"error": str(e)}]
