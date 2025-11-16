"""Minority class visualization helpers."""

from typing import Dict


def summarize_minorities(metrics: Dict[str, float]) -> str:
    """Summarize minority performance metrics as text."""
    return ", ".join(f"{k}: {v:.2f}" for k, v in metrics.items())
