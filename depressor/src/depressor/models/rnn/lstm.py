"""LSTM encoder for text classification baselines."""

from typing import Any
import torch.nn as nn


class LSTMEncoder(nn.Module):
    def __init__(self, vocab_size: int, hidden_size: int) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)

    def forward(self, x: Any) -> Any:
        embedded = self.embedding(x)
        outputs, _ = self.lstm(embedded)
        return outputs
