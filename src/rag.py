from pathlib import Path
import re
from collections import Counter

KB_PATH = (
    Path(__file__).resolve().parent.parent
    / "knowledge_base"
    / "it_support_faq.txt"
)


def _tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def load_entries():
    text = KB_PATH.read_text(encoding="utf-8")
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]

    entries = []

    for block in blocks:
        lines = block.splitlines()
        title = lines[0].strip()
        body = " ".join(x.strip() for x in lines[1:])
        entries.append((title, body))

    return entries


def retrieve(query, k=3):
    q = Counter(_tokens(query))
    scored = []

    for title, body in load_entries():
        words = Counter(_tokens(title + " " + body))
        overlap = sum(min(q[w], words[w]) for w in q)
        scored.append((overlap, title, body))

    scored.sort(reverse=True)

    return [
        {"title": title, "text": body, "score": score}
        for score, title, body in scored[:k]
        if score > 0
  ]
