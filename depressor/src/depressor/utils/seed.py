"""Deterministic seed handling."""

import os
import random
import numpy as np


def set_seed(seed: int) -> None:
    """Set seeds for reproducibility across libraries."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
