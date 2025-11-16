#!/usr/bin/env python
"""Reproduces figures for reports and dashboards."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate figures")
    parser.add_argument("--output", type=Path, required=True, help="Output directory for figures")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Generating figures into {args.output}")


if __name__ == "__main__":
    main()
