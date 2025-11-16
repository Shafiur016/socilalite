"""DeBERTa encoder augmented with a BiLSTM head."""

from typing import Any, Dict
import torch.nn as nn


class DebertaBiLSTM(nn.Module):
    def __init__(self, model_name: str = "microsoft/deberta-v3-base", hidden_size: int = 768) -> None:
        super().__init__()
        self.model_name = model_name
        self.bilstm = nn.LSTM(hidden_size, hidden_size // 2, num_layers=1, bidirectional=True, batch_first=True)

    def forward(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        outputs, _ = self.bilstm(inputs.get("hidden", None)) if isinstance(inputs, dict) else (None, None)
        return {"model": self.model_name, "lstm_output": outputs}
