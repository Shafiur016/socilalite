"""Validation-weighted soft voting ensemble."""

from typing import Dict, List
import numpy as np


def soft_vote(predictions: List[np.ndarray], weights: List[float]) -> np.ndarray:
    """Compute a weighted average of prediction arrays."""
    stacked = np.stack(predictions)
    weight_array = np.array(weights).reshape(len(weights), 1)
    return (stacked * weight_array).sum(axis=0) / weight_array.sum()
