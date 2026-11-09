from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 


@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor"  : "Deyvi Rivera",
            "version": "0.1.0"}
        
@router.get("/deyvi")
def endpoint_deyvi() -> Mensaje:
    return Mensaje(texto="Hola", campo_interno="desde Deyvi link")

@router.get("/rivera", response_model=Mensaje)
def endpoint_rivera():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "imprime desde endpoint Rivera"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no debería salir"}