from pydantic import BaseModel
from typing import List


class Comic(BaseModel):
    id: int
    title: str
    type: str  # manhwa,manhua,manga
    genres: List[str]
    setting: str  # murim,modern,historical,fantasy
    pacing: str  # slow ,medium,fast
    art_style: str  #clean,detailed,crowded 
    tone: str  # light,dark,balanced
    summary: str