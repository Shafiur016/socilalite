"""Oversampling helpers for imbalanced datasets."""

from typing import List


def oversample(indices: List[int], ratio: float = 0.5) -> List[int]:
    """Return a simple oversampled index list."""
    return indices + indices[: int(len(indices) * ratio)]
