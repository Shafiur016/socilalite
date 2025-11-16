"""TorchServe handler stub for Depressor models."""

from typing import Any, List


class ModelHandler:
    def __init__(self) -> None:
        self.initialized = False

    def initialize(self, ctx: Any) -> None:  # pylint: disable=unused-argument
        self.initialized = True

    def handle(self, data: List[Any], context: Any = None) -> List[Any]:  # pylint: disable=unused-argument
        return data
