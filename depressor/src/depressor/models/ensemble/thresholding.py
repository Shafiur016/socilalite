"""Threshold search utilities for multi-label tasks."""

import numpy as np


def apply_thresholds(logits: np.ndarray, thresholds: np.ndarray) -> np.ndarray:
    """Apply per-class thresholds to logits."""
    return (logits >= thresholds).astype(int)
