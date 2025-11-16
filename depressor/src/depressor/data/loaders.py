"""Dataset readers for Reddit and related sources."""

import json
from pathlib import Path
from typing import List
from .schemas import TextExample


def load_jsonl(path: Path) -> List[TextExample]:
    """Load a JSONL file into structured examples."""
    examples: List[TextExample] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        payload = json.loads(line)
        examples.append(TextExample(text=payload["text"], labels=payload.get("labels", [])))
    return examples
