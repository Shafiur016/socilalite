#!/usr/bin/env python
"""Runs leave-one-backbone-out experiments to assess ensemble robustness."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run LOBO experiments")
    parser.add_argument("--ensemble-config", type=Path, required=True, help="Ensemble configuration")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Running LOBO with ensemble config: {args.ensemble_config}")


if __name__ == "__main__":
    main()
