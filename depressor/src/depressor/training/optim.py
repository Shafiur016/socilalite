"""Optimizer configuration helpers."""

from typing import Any


def build_optimizer(model: Any, lr: float = 2e-5, weight_decay: float = 0.01) -> dict:
    """Return a placeholder optimizer configuration."""
    return {"model": model, "lr": lr, "weight_decay": weight_decay}
