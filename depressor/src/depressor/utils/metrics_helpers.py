"""Helper utilities for computing confidence intervals and bootstrapping."""

from typing import List, Tuple
import numpy as np


def bootstrap_ci(values: List[float], alpha: float = 0.05) -> Tuple[float, float]:
    """Compute a simple bootstrap confidence interval."""
    if not values:
        return (0.0, 0.0)
    samples = np.random.choice(values, size=(1000, len(values)), replace=True)
    lower = np.percentile(samples.mean(axis=1), alpha / 2 * 100)
    upper = np.percentile(samples.mean(axis=1), (1 - alpha / 2) * 100)
    return float(lower), float(upper)
