from fastapi import FastAPI
from routers.hello_world import router
from routers.task_router import tasks_router
from routers.inventario import inventario_router

app = FastAPI(title="API Control de Inventario")

app.include_router(router)
app.include_router(tasks_router)
app.include_router(inventario_router)
