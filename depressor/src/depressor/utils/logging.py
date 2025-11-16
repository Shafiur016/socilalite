"""Lightweight logging utilities built on top of loguru."""

from loguru import logger


def init_logger(level: str = "INFO") -> None:
    """Initialize the loguru logger with the chosen level."""
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=level)
