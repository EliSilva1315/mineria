from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="API – Predicción de Ingresos",
    description="API REST para predecir el ingreso estimado de una transacción.",
    version="1.0"
)

# Cargar el modelo entrenado
#modelo = joblib.load("model/modelo_tipvos.pkl")  

# Definir el esquema de entrada usando Pydantic
class InputData(BaseModel):
    quantity: int
    price: float
    stock: int
    age: int
    pages_viewed: int
    duration_seconds: float
    days_since_signup: int
    customer_age_group_18_25: int
    customer_age_group_26_40: int
    customer_age_group_41_60: int
    device_mobile: int
    device_desktop: int
    region_sierra: int
    region_costa: int
    region_oriente: int

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de predicción de ingresos"}

@app.post("/predict")
def predict(data: InputData):
    # Convertir la entrada en DataFrame
    df = pd.DataFrame([data.dict()])

    # Predecir con el modelo
    prediction = modelo.predict(df)

    return {
        "revenue_estimado": round(prediction[0], 2)
    }
