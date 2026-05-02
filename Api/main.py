from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open("E:/personal document/placement program/house price prediction using regression model/models/simple_model.pkl", "rb") as f:
    model = pickle.load(f)

# Input schema
class HouseData(BaseModel):
    data: dict

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}

@app.post("/predict")
def predict(house: HouseData):
    try:
        input_df = pd.DataFrame([house.data])
        prediction = model.predict(input_df)[0]

        return {"predicted_price": float(prediction)}

    except Exception as e:
        return {"error": str(e)}
    input_df = pd.DataFrame([house.data])