import re
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
SKIP_FILES = {"README.md", "INDEX.md"}
SKIP_DIRS = {"scripts", ".git"}


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text()
    match = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not match:
        return None

    meta = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [t.strip() for t in value[1:-1].split(",")]
        meta[key.strip()] = value
    return meta


def build_index() -> str:
    entries = []
    for md in sorted(VAULT_ROOT.rglob("*.md")):
        if md.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIRS for part in md.relative_to(VAULT_ROOT).parts):
            continue

        meta = parse_frontmatter(md)
        if not meta:
            continue

        rel = md.relative_to(VAULT_ROOT)
        summary = meta.get("summary", "—")
        tags = meta.get("tags", [])
        tags_str = ", ".join(f"`{t}`" for t in tags) if isinstance(tags, list) else tags
        date = meta.get("date", "—")
        entries.append(f"| [{rel}]({rel}) | {summary} | {tags_str} | {date} |")

    lines = [
        "# Index\n",
        "| File | Summary | Tags | Date |",
        "|------|---------|------|------|",
        *entries,
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    index_path = VAULT_ROOT / "INDEX.md"
    index_path.write_text(build_index())
