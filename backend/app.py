from fastapi import FastAPI
import json
import os

app = FastAPI()

@app.get("/")
def home():

    data = [
        {
            "id": 1,
            "title": "MediTrack"
        },
        {
            "id": 2,
            "title": "Portfolio updated"
        }
    ]

    os.makedirs("backend/data", exist_ok=True)

    with open(
        "backend/data/project.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    return {
        "status": "saved",
        "records": len(data)
    }