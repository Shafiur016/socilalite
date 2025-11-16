"""Heatmap rendering helpers for token attributions."""

from typing import List


def render_heatmap(tokens: List[str], scores: List[float]) -> str:
    """Return a textual heatmap representation."""
    return " ".join(f"{t}({s:.2f})" for t, s in zip(tokens, scores))
