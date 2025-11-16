"""Stability metrics for attribution methods."""

from typing import List
import numpy as np


def overlap_at_k(topk_a: List[int], topk_b: List[int], k: int) -> float:
    """Compute overlap@k between two attribution rankings."""
    return len(set(topk_a[:k]) & set(topk_b[:k])) / float(k or 1)


def kendall_tau(a: List[int], b: List[int]) -> float:
    """Simplified Kendall's tau using numpy."""
    if len(a) != len(b):
        return 0.0
    arr_a = np.array(a)
    arr_b = np.array(b)
    return float(np.corrcoef(arr_a, arr_b)[0, 1])
