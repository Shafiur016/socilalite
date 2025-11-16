"""Simple timing helpers for profiling."""

import time
from contextlib import contextmanager
from typing import Iterator


def now() -> float:
    return time.perf_counter()


@contextmanager
def timer(name: str) -> Iterator[None]:
    start = now()
    yield
    elapsed = now() - start
    print(f"[{name}] {elapsed:.4f}s")
