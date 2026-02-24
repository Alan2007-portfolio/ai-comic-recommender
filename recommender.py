from typing import List, Optional
from models import Comic
from data import comics


def filter_comics(
    type: Optional[str] = None,
    setting: Optional[str] = None,
    tone: Optional[str] = None,
    pacing: Optional[str] = None,
    genre: Optional[str] = None
) -> List[Comic]:

    results = comics

    if type:
        results = [c for c in results if c.type.lower() == type.lower()]

    if setting:
        results = [c for c in results if c.setting.lower() == setting.lower()]

    if tone:
        results = [c for c in results if c.tone.lower() == tone.lower()]

    if pacing:
        results = [c for c in results if c.pacing.lower() == pacing.lower()]

    if genre:
        results = [
            c for c in results
            if genre.lower() in [g.lower() for g in c.genres]
        ]

    return results