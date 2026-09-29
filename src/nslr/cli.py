from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

from .io import read_text, save_json_new
from .parser import compile_source


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="nsl",
        description="Compile bounded scientific intent into typed Notation Systems contracts.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    compile_cmd = commands.add_parser("compile")
    compile_cmd.add_argument("source", type=Path)
    compile_cmd.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        result = compile_source(read_text(args.source))
        save_json_new(args.output, result)
        print(json.dumps({
            "status": "compiled",
            "language": result["language"],
            "output_schema": result["output_schema"],
            "output": str(args.output),
            "provider_execution": False,
        }))
        return 0
    except (OSError, ValueError, UnicodeError) as exc:
        print(json.dumps({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
