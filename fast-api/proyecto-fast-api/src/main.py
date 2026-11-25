# app/main.py
from fastapi import FastAPI

app = FastAPI(title="Curso FastAPI + uv")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", "autor": "Ing. Deyvi Rivera", "Version": "0.1.0"}

@app.get("/deyvi")
def endpoint_a() -> Mensaje:
    return Mensaje(texto="Hola")


@app.get("/rivera", response_model=Mensaje)
def endpoint_b():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "no debería salir"}