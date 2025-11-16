"""Text normalization helpers for social media content."""

import re

URL_RE = re.compile(r"https?://\S+")
USER_RE = re.compile(r"@[A-Za-z0-9_]+")
NUM_RE = re.compile(r"\d+")


def normalize(text: str) -> str:
    """Apply light normalization with placeholder tokens."""
    text = URL_RE.sub("<URL>", text)
    text = USER_RE.sub("<USER>", text)
    text = NUM_RE.sub("<NUM>", text)
    return text.lower()
