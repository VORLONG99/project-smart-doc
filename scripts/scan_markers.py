#!/usr/bin/env python3
"""Scan repository files for technical-debt markers."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_MARKERS = ["TODO", "FIXME", "HACK", "NOTE", "XXX", "DEPRECATED"]
DEFAULT_EXCLUDES = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    ".next",
    ".nuxt",
    "coverage",
    "__pycache__",
}
TEXT_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".rs",
    ".rb",
    ".php",
    ".c",
    ".cc",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".swift",
    ".kt",
    ".kts",
    ".scala",
    ".sh",
    ".bash",
    ".zsh",
    ".yml",
    ".yaml",
    ".toml",
    ".ini",
    ".cfg",
    ".conf",
    ".env",
    ".md",
    ".txt",
}


def build_pattern(markers: list[str]) -> re.Pattern[str]:
    escaped = "|".join(re.escape(m) for m in markers)
    return re.compile(rf"\b({escaped})\b")


def should_scan_file(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    return path.name in {"Dockerfile", "Makefile"}


def scan_repo(root: Path, markers: list[str], excludes: set[str]) -> list[dict]:
    pattern = build_pattern(markers)
    findings: list[dict] = []

    for path in root.rglob("*"):
        if any(part in excludes for part in path.parts):
            continue
        if not should_scan_file(path):
            continue

        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for idx, line in enumerate(content.splitlines(), start=1):
            match = pattern.search(line)
            if not match:
                continue
            findings.append(
                {
                    "marker": match.group(1),
                    "file": str(path.relative_to(root)),
                    "line": idx,
                    "text": line.strip(),
                }
            )
    return findings


def print_markdown(findings: list[dict]) -> None:
    total = len(findings)
    by_marker = Counter(item["marker"] for item in findings)
    by_file: dict[str, list[dict]] = defaultdict(list)
    for item in findings:
        by_file[item["file"]].append(item)

    print("# Marker Scan Report")
    print()
    print(f"- Total findings: {total}")
    if total == 0:
        return

    print("- By marker:")
    for marker, count in sorted(by_marker.items()):
        print(f"  - {marker}: {count}")

    print()
    print("## Details by file")
    for file in sorted(by_file.keys()):
        print()
        print(f"### `{file}`")
        for item in by_file[file]:
            text = item["text"][:200]
            print(f"- L{item['line']} [{item['marker']}] {text}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan source files for marker comments.")
    parser.add_argument("root", nargs="?", default=".", help="Project root path")
    parser.add_argument(
        "--markers",
        default=",".join(DEFAULT_MARKERS),
        help="Comma-separated markers to scan",
    )
    parser.add_argument(
        "--exclude",
        default=",".join(sorted(DEFAULT_EXCLUDES)),
        help="Comma-separated directory names to ignore",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    markers = [m.strip() for m in args.markers.split(",") if m.strip()]
    excludes = {e.strip() for e in args.exclude.split(",") if e.strip()}

    findings = scan_repo(root, markers, excludes)

    if args.format == "json":
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return
    print_markdown(findings)


if __name__ == "__main__":
    main()
