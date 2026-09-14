from fastapi import FastAPI
from models import Transferencia

app = FastAPI()

@app.get("/")
def inicio():
    return {"Mensaje": "API de prueba"} 

transferencias = []
@app.get("/api/transferencias")
def listar_trasnferencias():
        return transferencias

@app.post("/api/transferencias")
def crear_transferencia(transferencia: Transferencia):
    transferencias.append(transferencia)
    return transferencia