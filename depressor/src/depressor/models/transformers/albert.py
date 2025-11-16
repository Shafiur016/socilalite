"""ALBERT backbone wrapper."""

from typing import Any, Dict
import torch.nn as nn


class AlbertBackbone(nn.Module):
    def __init__(self, model_name: str = "albert-base-v2") -> None:
        super().__init__()
        self.model_name = model_name

    def forward(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {"model": self.model_name, "inputs": inputs}
