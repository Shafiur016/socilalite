"""Near-duplicate detection helpers."""

from typing import Iterable, List


def drop_duplicates(lines: Iterable[str]) -> List[str]:
    """Remove exact duplicates while preserving order."""
    seen = set()
    unique: List[str] = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            unique.append(line)
    return unique
