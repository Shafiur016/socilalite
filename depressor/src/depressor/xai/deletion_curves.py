"""Compute deletion curves for attribution faithfulness."""

from typing import List
import numpy as np


def deletion_auc(scores: List[float]) -> float:
    """Return area under a simple deletion curve."""
    if not scores:
        return 0.0
    return float(np.trapz(scores))
