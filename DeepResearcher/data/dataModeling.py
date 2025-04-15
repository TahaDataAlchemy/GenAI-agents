from pydantic import BaseModel, Field
from typing import Optional, TypedDict

class SearchInput(BaseModel):
    """
    Model for the user input. Either a search query or a direct link must be provided.
    """
    query: str = Field(..., description="Search query provided by the user")
    site: Optional[str] = Field(None, description="Optional direct link to fetch data from")
    max_results: Optional[int] = Field(1, gt=0, le=50, description="Number of results to fetch (1-50)")


class UserResponseApi(TypedDict):
    """
    TypedDict for defining the expected structure of the user's response.
    """
    text: str
