"""Evaluation metrics for classification tasks."""

from typing import Dict, List
import numpy as np


def macro_f1(preds: np.ndarray, labels: np.ndarray) -> float:
    """Compute a simple macro-F1 placeholder."""
    if preds.size == 0 or labels.size == 0:
        return 0.0
    return float(np.mean(preds == labels))


def per_class_accuracy(preds: np.ndarray, labels: np.ndarray, classes: List[str]) -> Dict[str, float]:
    """Return per-class accuracy dictionary."""
    metrics: Dict[str, float] = {}
    for idx, cls in enumerate(classes):
        mask = labels == idx
        metrics[cls] = float(np.mean(preds[mask] == labels[mask])) if mask.any() else 0.0
    return metrics
