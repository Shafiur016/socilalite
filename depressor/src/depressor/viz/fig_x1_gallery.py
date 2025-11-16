"""Visualization helpers for true/false/borderline example galleries."""

from typing import List


def render_gallery(examples: List[str]) -> str:
    """Return a textual representation of a gallery."""
    return "\n".join(examples)
