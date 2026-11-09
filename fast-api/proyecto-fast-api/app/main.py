# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Curso FastAPI + uv")


class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv"}

@app.get("/deyvi")
def endpoint_a() -> Mensaje:
    return Mensaje(texto="Hola")


@app.get("/rivera", response_model=Mensaje)
def endpoint_b():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "no debería salir"}