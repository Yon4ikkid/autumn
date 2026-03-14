from pydantic import BaseModel
from typing import Optional
from abc import ABC, abstractmethod


class Repository(BaseModel):
    name: str | None = None
