from pydantic import BaseModel
from typing import List,Optional
class State(BaseModel):
    text: str
    classification: Optional[str] = None
    entities: Optional[List[str]] = None
    summary: Optional[str] = None


class TextInput(BaseModel):
    text:str

class TextProcessingResponseAPI(BaseModel):
    classification: str
    entities: list[str]
    summary: str
