from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# @app.get("api/estimate/{square_metter}/{nb_rooms}/{surface}/{zip}")
# def estimate(square_metter, nb_rooms, surface, zip, q: Optional[str] = None):
#     return {"item_id": square_metter, "q": q}

@app.get("/api/estimate/{surface_carrez}/{nb_rooms}/{surface}/{zip}")
def estimate(surface_carrez: int, nb_rooms: int, surface: int, zip: str):
    # { "estimation": "130 000€" }
    return {"surface_carrez": surface_carrez, "nb_rooms": nb_rooms, "surface": surface, "zip": zip}
