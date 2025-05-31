
from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("anomaly_model.pkl")

@app.post("/score")
async def score(request: Request):
    data = await request.json()
    input_data = data.get("input_data")
    df = pd.DataFrame(input_data["values"], columns=input_data["columns"])
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    predictions = model.decision_function(df)
    scores = model.predict(df)

    result = [{
        "score": float(pred),
        "risk_level": "High" if pred < -0.2 else "Low"
    } for pred in predictions]

    return {"result": result}
