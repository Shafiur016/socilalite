#!/usr/bin/env python
"""Trains a single transformer backbone model using the provided YAML config."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a backbone model")
    parser.add_argument("--config", type=Path, required=True, help="Path to model config")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Training backbone with config: {args.config}")


if __name__ == "__main__":
    main()
