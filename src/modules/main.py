import pandas as pd
import pickle
from typing import Optional
from fastapi import FastAPI

OUT_LOCAL_PATH = 'data/OUT/'
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/estimate/")
def estimate(metre_carre: Optional[int] = None, nb_pieces: Optional[int] = None, terrain: Optional[int] = None, code_postal: Optional[int] = None):
    loaded_model_house = pickle.load(open(f'{OUT_LOCAL_PATH}house.pkl', 'rb'))
    loaded_model_apartment = pickle.load(
        open(f'{OUT_LOCAL_PATH}apartment.pkl', 'rb'))

    predict_house = loaded_model_house.predict(
        [[code_postal, metre_carre, nb_pieces]])

    predict_apartment = loaded_model_apartment.predict(
        [[code_postal, metre_carre, nb_pieces]])

    return {"estimation_house": f'{round(predict_house[0])}€', "estimation_apartment":  f'{round(predict_apartment[0])}€'}
