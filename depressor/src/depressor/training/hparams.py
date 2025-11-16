"""Hyperparameter utilities."""

from typing import Dict, List


def grid_search(space: Dict[str, List]) -> List[Dict[str, object]]:
    """Generate a simple Cartesian product of hyperparameters."""
    combos: List[Dict[str, object]] = []
    keys = list(space.keys())
    if not keys:
        return combos
    first, *rest = keys
    for value in space[first]:
        if rest:
            for sub in grid_search({k: space[k] for k in rest}):
                combo = {first: value}
                combo.update(sub)
                combos.append(combo)
        else:
            combos.append({first: value})
    return combos
