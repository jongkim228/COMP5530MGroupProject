"""Turn docs/decisions.md into a Markdown table.

Usage:
    python scripts/decisions_to_table.py                 # prints the table
    python scripts/decisions_to_table.py --out docs/decisions-table.md

Expects each decision in this format:

    # Title
    - **Date:** ...
    - **Decision:** ...
    - **Alternatives considered:** ...
    - **Reason:** ...
    - **Any other field:** ...      (optional, becomes its own column)
"""
import argparse
import re
from pathlib import Path

FIELD = re.compile(r"^\s*-\s*\*\*(.+?):\*\*\s*(.*)$")


def parse(text: str) -> list[dict]:
    entries, current, last_field = [], None, None
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            if title.lower() == "decision log":
                continue
            current = {"Title": title}
            entries.append(current)
            last_field = None
        elif current is not None and (m := FIELD.match(line)):
            last_field = m.group(1).strip()
            current[last_field] = m.group(2).strip()
        elif current is not None and last_field and line.startswith("  ") and line.strip():
            current[last_field] += " " + line.strip()  # wrapped continuation line
    return entries


def to_table(entries: list[dict]) -> str:
    columns = ["#", "Title"]
    for e in entries:
        for key in e:
            if key not in columns:
                columns.append(key)
    rows = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    for i, e in enumerate(entries, 1):
        cells = [str(i)] + [e.get(c, "").replace("|", "\\|") for c in columns[1:]]
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="docs/decisions.md")
    parser.add_argument("--out")
    args = parser.parse_args()
    table = to_table(parse(Path(args.src).read_text(encoding="utf-8")))
    if args.out:
        Path(args.out).write_text("# Decision log (table)\n\nGenerated from decisions.md; do not edit by hand.\n\n" + table, encoding="utf-8")
    else:
        print(table)


if __name__ == "__main__":
    main()
