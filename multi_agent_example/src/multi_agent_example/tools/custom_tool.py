from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel
import random


class RandomNumberToolInput(BaseModel):
    pass

class RandomNumberTool(BaseTool):
    name: str = "Random Number Generator"
    description: str = "Use this tool when you need a random number."
    args_schema: Type[BaseModel] = RandomNumberToolInput

    def _run(self) -> int:
        return random.randint(1, 20)
