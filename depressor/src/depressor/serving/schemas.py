"""Pydantic models for serving requests and responses."""

from pydantic import BaseModel
from typing import List


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    labels: List[str]
    scores: List[float]
