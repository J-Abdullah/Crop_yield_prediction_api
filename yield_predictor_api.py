from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from joblib import load

predictor = load('yield_predictor.joblib')
area_encoder = load('area_encoder.joblib')
item_encoder = load('item_encoder.joblib')

app=FastAPI()

class YieldPredictionRequest(BaseModel):
    area: str
    item: str
    avg_rain: float
    pesticides: float
    temperature: float
    
@app.post("/predict/")
def predict_yield(request: YieldPredictionRequest):
    try:
        area_encoded=area_encoder.transform([request.area.lower()])
        item_encode=item_encoder.transform([request.item.lower()])
        
        prediction=predictor.predict([[area_encoded[0],item_encode[0],request.avg_rain,request.pesticides,request.temperature]])
        return {"predicted_yield":prediction[0]}     
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))