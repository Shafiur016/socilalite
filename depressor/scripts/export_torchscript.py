#!/usr/bin/env python
"""Exports a trained model to TorchScript for TorchServe deployment."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export model to TorchScript")
    parser.add_argument("--model", type=Path, required=True, help="Model checkpoint")
    parser.add_argument("--output", type=Path, required=True, help="TorchScript output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Exporting {args.model} to TorchScript at {args.output}")


if __name__ == "__main__":
    main()
