from pydantic import BaseModel, Field
from typing import Optional, TypedDict

class TextInput(BaseModel):
    """
    Model for the user input. Either a search query or a direct link must be provided.
    """
    query: str = Field(..., description="Search query provided by the user")
    link: Optional[str] = Field(None, description="Optional direct link to fetch data from")

class UserResponseApi(TypedDict):
    """
    TypedDict for defining the expected structure of the user's response.
    """
    text: str
