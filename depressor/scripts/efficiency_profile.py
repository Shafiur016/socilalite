#!/usr/bin/env python
"""Profiles inference efficiency, including time, VRAM, and estimated energy."""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile model efficiency")
    parser.add_argument("--model", type=Path, required=True, help="Model checkpoint")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Profiling efficiency for {args.model}")


if __name__ == "__main__":
    main()
