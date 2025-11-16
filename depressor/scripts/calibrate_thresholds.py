#!/usr/bin/env python
"""Calibrates per-class thresholds for multi-label predictions."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calibrate thresholds")
    parser.add_argument("--val-preds", type=Path, required=True, help="Validation predictions path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Calibrating thresholds from {args.val_preds}")


if __name__ == "__main__":
    main()
