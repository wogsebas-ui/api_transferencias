from fastapi import FastAPI, HTTPException
from models import Transferencia
from database import guardar_transferencia, obtener_transferencias, obtener_transferencia, actualizar_transferencia, inhabilitar_transferencia

app = FastAPI()

@app.get("/")
def inicio():
    return {"Mensaje": "API de prueba"} 

transferencias = []
@app.get("/api/transferencias")
def listar_transferencias():
        return obtener_transferencias()

@app.get("/api/transferencias/{id_pago}")
def buscar_transferencia(id_pago: str):
         transferencia = obtener_transferencia(id_pago)
         if transferencia is None:
            raise HTTPException(status_code=404, detail="Transferencia no encontrada")
         return transferencia

     
     
    

@app.post("/api/transferencias", status_code=201)
def crear_transferencia(transferencia: Transferencia):
    guardar_transferencia(transferencia)
    return transferencia


@app.put("/api/transferencias/{id_pago}")
def actulizar(id_pago: str, transferencia: Transferencia):
    filas_actualizadas = actualizar_transferencia(id_pago, transferencia)

    if filas_actualizadas == 0:
         raise HTTPException(status_code=404, detail="Transferencia no encontrada")
    return transferencia

@app.delete("/api/transferencias/{id_pago}")
def eliminar_transferencia(id_pago: str):
    filas_actualizadas = inhabilitar_transferencia(id_pago)

    if filas_actualizadas == 0:
        raise HTTPException(status_code=404, detail="Transferencia no encontrada")
    return {"mensaje": "Transferencia inhabilitada correctamente",
            "id_pago": id_pago,
            "estado": "inactiva"
    }
