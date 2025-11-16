"""Training loop utilities."""

from typing import Any


def train_one_epoch(model: Any, dataloader: Any) -> None:
    """Placeholder training loop."""
    print(f"Training {model} on {len(dataloader) if dataloader is not None else 0} batches")
