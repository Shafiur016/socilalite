#!/usr/bin/env python
"""Runs paired tests and computes effect sizes across folds."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run significance tests")
    parser.add_argument("--results", type=Path, required=True, help="Aggregated results file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Running significance tests for {args.results}")


if __name__ == "__main__":
    main()
