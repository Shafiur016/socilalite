"""Utility helpers for loading and saving common file formats."""

from pathlib import Path
from typing import Any, Dict, Iterable
import json
import csv


def load_json(path: Path) -> Any:
    """Load JSON content from a file path."""
    with path.open("r", encoding="utf-8") as fp:
        return json.load(fp)


def save_json(path: Path, payload: Any) -> None:
    """Save JSON payload to disk with UTF-8 encoding."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fp:
        json.dump(payload, fp, ensure_ascii=False, indent=2)


def write_rows(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    """Persist an iterable of dictionaries as CSV rows."""
    path.parent.mkdir(parents=True, exist_ok=True)
    items = list(rows)
    if not items:
        return
    with path.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=list(items[0].keys()))
        writer.writeheader()
        writer.writerows(items)
