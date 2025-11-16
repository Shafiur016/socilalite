#!/usr/bin/env python
"""Evaluates predictions with micro/macro metrics and per-class tables."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate model outputs")
    parser.add_argument("--config", type=Path, required=True, help="Dataset configuration")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Evaluating using config: {args.config}")


if __name__ == "__main__":
    main()
