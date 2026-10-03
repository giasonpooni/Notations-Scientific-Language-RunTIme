from __future__ import annotations
import json
import os
from pathlib import Path
import tempfile

MAX_BYTES = 128 * 1024


def read_text(path: Path) -> str:
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError("Scientific source must be a regular file")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    if not raw or len(raw) > MAX_BYTES:
        raise ValueError("Scientific source file exceeds 128 KiB or is empty")
    return raw.decode("utf-8")


def save_json_new(path: Path, value: dict) -> None:
    raw = (json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".nslr-", dir=path.parent) as directory:
        staged = Path(directory) / "result.json"
        with staged.open("xb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.link(staged, path)
