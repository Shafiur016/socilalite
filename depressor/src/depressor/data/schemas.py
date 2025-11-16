"""Data schemas for examples and labels."""

from dataclasses import dataclass
from typing import List


@dataclass
class TextExample:
    text: str
    labels: List[str]
