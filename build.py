from __future__ import annotations

import json
from html import escape
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "template.html"
PAPERS_PATH = BASE_DIR / "papers.json"
OUTPUT_PATH = BASE_DIR / "index.html"
PLACEHOLDER = "{{PUBLICATIONS}}"


def build_publications_html(papers: list[dict[str, str]]) -> str:
    lines = []
    for paper in papers:
        title = escape(paper["title"])
        author = escape(paper["author"])
        conf = escape(paper["conf"])
        lines.append(
            "      <li>"
            f"<strong>{title}</strong><br>"
            f"<em>{author}</em> · {conf}"
            "</li>"
        )
    return "\n".join(lines)


def main() -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    papers = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
    publications_html = build_publications_html(papers)

    if PLACEHOLDER not in template:
        raise ValueError(f"Placeholder {PLACEHOLDER!r} was not found in template.html")

    output = template.replace(PLACEHOLDER, publications_html)
    OUTPUT_PATH.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
