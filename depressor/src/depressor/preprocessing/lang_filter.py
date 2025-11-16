"""Language filtering utilities."""

from typing import Iterable, List, Tuple


def filter_by_lang(pairs: Iterable[Tuple[str, float]], threshold: float = 0.95) -> List[str]:
    """Keep texts whose language confidence exceeds the threshold."""
    return [text for text, score in pairs if score >= threshold]
