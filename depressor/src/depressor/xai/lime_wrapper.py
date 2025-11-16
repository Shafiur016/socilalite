"""LIME explanation utilities."""

from typing import List


def explain_text(text: str, labels: List[str]) -> dict:
    """Return a placeholder explanation structure."""
    return {"text": text, "labels": labels, "attributions": []}
