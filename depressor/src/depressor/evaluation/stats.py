"""Statistical testing utilities."""

from typing import Tuple
import numpy as np
from scipy import stats


def paired_t_test(a: np.ndarray, b: np.ndarray) -> Tuple[float, float]:
    """Run a paired t-test between two result arrays."""
    t_stat, p_val = stats.ttest_rel(a, b)
    return float(t_stat), float(p_val)
