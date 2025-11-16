"""Sigmoid classification head for multi-label tasks."""

from typing import Any
import torch.nn as nn


class MultiLabelHead(nn.Module):
    def __init__(self, hidden_size: int, num_labels: int) -> None:
        super().__init__()
        self.dropout = nn.Dropout(0.3)
        self.classifier = nn.Linear(hidden_size, num_labels)

    def forward(self, x: Any) -> Any:
        return self.classifier(self.dropout(x))
