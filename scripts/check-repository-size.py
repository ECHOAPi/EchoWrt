#!/usr/bin/env python3
"""Keep tracked source small; generated firmware and build trees stay outside Git."""

from pathlib import Path
import subprocess
import sys

MAX_FILE_BYTES = 512 * 1024
MAX_TOTAL_BYTES = 2 * 1024 * 1024
GENERATED_ROOTS = {"openwrt", "dl", "bin", "build_dir", "staging_dir", "tmp", "firmware"}
BINARY_SUFFIXES = (".img", ".img.gz", ".iso", ".zip", ".7z", ".tar", ".tar.gz", ".tar.xz")


def check_entries(entries):
    errors = []
    total = 0
    for name, size in entries:
        total += size
        if name.split("/", 1)[0] in GENERATED_ROOTS or name.lower().endswith(BINARY_SUFFIXES):
            errors.append(f"Generated build output must not be tracked: {name}")
        if size > MAX_FILE_BYTES:
            errors.append(f"Tracked file exceeds 512 KiB: {name}")
    if total > MAX_TOTAL_BYTES:
        errors.append(f"Tracked source exceeds 2 MiB: {total} bytes")
    if errors:
        raise ValueError("\n".join(errors))
    return total


def main():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root,
                            check=True, capture_output=True)
    names = [name.decode("utf-8") for name in result.stdout.split(b"\0") if name]
    if not names:
        raise ValueError("No tracked files found; stage the source before checking")
    total = check_entries([(name, (root / name).stat().st_size) for name in names])
    print(f"Repository size check passed: {len(names)} files, {total} bytes.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Repository size check failed: {error}", file=sys.stderr)
        sys.exit(1)
