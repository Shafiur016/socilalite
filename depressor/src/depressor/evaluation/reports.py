"""Reporting utilities for metrics tables."""

from typing import Dict, List
from ..utils.io import write_rows
from pathlib import Path


def save_metrics_table(rows: List[Dict[str, object]], path: Path) -> None:
    """Persist metrics as a CSV table."""
    write_rows(path, rows)
