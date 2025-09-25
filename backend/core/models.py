from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option shown to the user")
    nextNode: Dict[str, Any] = Field(
        description="the node content and its options")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="the main content of the story node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinning: bool = Field(
        description="Whether this node is a winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(
        default=None, description="The options for this node")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")
