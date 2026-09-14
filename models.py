from pydantic import BaseModel
class Transferencia(BaseModel):
    cliente: str
    valor: float
    fecha: str
    hora: str       
    banco: str
    id_pago: str
    estado: str

