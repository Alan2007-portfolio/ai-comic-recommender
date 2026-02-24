from fastapi import FastAPI
from typing import Optional
from recommender import filter_comics

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AI Comic Recommender is running!"}


@app.get("/recommend")
def recommend(
    type: Optional[str] = None,
    setting: Optional[str] = None,
    tone: Optional[str] = None,
    pacing: Optional[str] = None,
    genre: Optional[str] = None
):
    results = filter_comics(type, setting, tone, pacing, genre)

    return {
        "count": len(results),
        "results": results
    }