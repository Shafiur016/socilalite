#!/usr/bin/env python
"""Executes ablation studies on sampling, class weights, and thresholding."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ablations")
    parser.add_argument("--config", type=Path, required=True, help="Training configuration")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Running ablation with config: {args.config}")


if __name__ == "__main__":
    main()
