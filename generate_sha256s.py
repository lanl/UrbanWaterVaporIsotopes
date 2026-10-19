#!/usr/bin/env python3
"""Generate SHA256SUMS.txt for the final UrbanWaterVaporIsotopes archive.

Run this script from the repository root *after* final cleanup. It hashes all
archived files except:
  - SHA256SUMS.txt itself
  - .git/ metadata
  - .ipynb_checkpoints/
  - __pycache__/
  - .DS_Store
  - output/cache/ (regenerable computational caches)
"""

from pathlib import Path
import hashlib

ROOT = Path.cwd().resolve()
OUT = ROOT / "SHA256SUMS.txt"

EXCLUDED_DIR_NAMES = {".git", ".ipynb_checkpoints", "__pycache__"}
EXCLUDED_RELATIVE_PREFIXES = {Path("output/cache")}
EXCLUDED_FILE_NAMES = {"SHA256SUMS.txt", ".DS_Store"}

CHUNK_SIZE = 16 * 1024 * 1024  # 16 MiB


def is_excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT)

    if path.name in EXCLUDED_FILE_NAMES:
        return True

    if any(part in EXCLUDED_DIR_NAMES for part in rel.parts):
        return True

    for prefix in EXCLUDED_RELATIVE_PREFIXES:
        try:
            rel.relative_to(prefix)
            return True
        except ValueError:
            pass

    return False


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            h.update(chunk)
    return h.hexdigest()


files = sorted(
    (p for p in ROOT.rglob("*") if p.is_file() and not is_excluded(p)),
    key=lambda p: p.relative_to(ROOT).as_posix(),
)

tmp = OUT.with_suffix(".txt.tmp")

with tmp.open("w", encoding="utf-8", newline="\n") as f:
    for i, path in enumerate(files, start=1):
        rel = path.relative_to(ROOT).as_posix()
        digest = sha256_file(path)
        f.write(f"{digest}  {rel}\n")
        print(f"[{i:>3}/{len(files)}] {rel}")

tmp.replace(OUT)

print(f"\nWrote {OUT}")
print(f"Hashed {len(files)} files.")
