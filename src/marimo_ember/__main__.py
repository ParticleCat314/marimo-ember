"""CLI: `marimo-ember install [DIR]` copies ember.css into DIR (default: theme/); `marimo-ember path`."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from marimo_ember import css_path

SNIPPET = """Add to pyproject.toml, then restart marimo:

[tool.marimo.display]
theme = "dark"
custom_css = ["{path}"]
"""


def main() -> None:
    parser = argparse.ArgumentParser(prog="marimo-ember")
    sub = parser.add_subparsers(dest="cmd", required=True)
    install = sub.add_parser("install", help="copy ember.css into a project directory")
    install.add_argument("dir", nargs="?", default="theme")
    sub.add_parser("path", help="print the bundled ember.css path")
    args = parser.parse_args()

    if args.cmd == "path":
        print(css_path())
        return
    dest = Path(args.dir) / "ember.css"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(css_path(), dest)
    print(f"wrote {dest}\n")
    print(SNIPPET.format(path=dest.as_posix()))


if __name__ == "__main__":
    main()
