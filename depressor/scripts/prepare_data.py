#!/usr/bin/env python
"""Preprocesses datasets and prepares stratified splits for training and evaluation."""

from pathlib import Path


def main() -> None:
    data_root = Path("data")
    print(f"Preparing data under {data_root.resolve()}")


if __name__ == "__main__":
    main()
