"""ROC and PR curve computation helpers."""

import numpy as np


def compute_curve_points(scores: np.ndarray, labels: np.ndarray) -> np.ndarray:
    """Return sorted score-label pairs as a placeholder curve."""
    order = np.argsort(-scores)
    return np.column_stack((scores[order], labels[order]))
