from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Page(BaseModel, Generic[T]):
    data: List[T]
    total: int
