#!/usr/bin/env python
"""Generates LIME explanations and deletion curves."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run LIME explainability")
    parser.add_argument("--model", type=Path, required=True, help="Model checkpoint")
    parser.add_argument("--data", type=Path, required=True, help="Data split for explanations")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Explaining {args.model} on {args.data}")


if __name__ == "__main__":
    main()
