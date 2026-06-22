from pydantic import BaseModel
from typing import List


class Architecture(BaseModel):
    entities: List[str]
    flows: List[str]
    modules: List[str]