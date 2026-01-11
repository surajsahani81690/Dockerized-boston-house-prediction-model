from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_inpu import UserInput
from model.model_prediction import model_prediction

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Prediction of housing prices in suburbs of Boston"}

@app.post("/predict")
def predict_housing(data: UserInput):

    user_input = data.dict()
    try:
        prediction = model_prediction(user_input)
        return JSONResponse(status_code=200,content = {"predicted_price":round(float(prediction),2)})
    except Exception as e:
        return JSONResponse(status_code=500,content = str(e))




