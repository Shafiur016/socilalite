"""Dashboard aggregation utilities."""

from typing import Dict


def summarize_metrics(metrics: Dict[str, float]) -> str:
    """Return a simple dashboard-style summary string."""
    return " | ".join(f"{k}: {v:.3f}" for k, v in metrics.items())
