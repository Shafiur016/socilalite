#!/usr/bin/env python
"""Fuses model outputs using validation-weighted soft voting."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fuse ensemble predictions")
    parser.add_argument("--config", type=Path, required=True, help="Ensemble configuration")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Fusing ensemble with config: {args.config}")


if __name__ == "__main__":
    main()
