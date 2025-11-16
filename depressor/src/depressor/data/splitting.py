"""Dataset splitting utilities, including iterative stratification."""

from typing import List, Tuple
import numpy as np


def iterative_stratification(labels: np.ndarray, folds: int) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Placeholder iterative stratification returning empty splits."""
    splits: List[Tuple[np.ndarray, np.ndarray]] = []
    for _ in range(folds):
        splits.append((np.array([], dtype=int), np.array([], dtype=int)))
    return splits
