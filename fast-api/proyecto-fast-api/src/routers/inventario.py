from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

inventario_router = APIRouter(prefix="/inventario", tags=["Inventario"])


class ProveedorCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    ciudad: str | None = None


class ProveedorRead(ProveedorCreate):
    id: int


class ProductoCreate(BaseModel):
    codigo: str = Field(min_length=3, max_length=20)
    nombre: str = Field(min_length=3, max_length=100)
    categoria: str
    precio: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)
    stock_minimo: int = Field(default=5, ge=0)
    proveedor_id: int | None = None


class ProductoRead(ProductoCreate):
    id: int
    stock_bajo: bool


class ProductoUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    categoria: str | None = None
    precio: float | None = Field(default=None, gt=0)
    stock_minimo: int | None = Field(default=None, ge=0)
    proveedor_id: int | None = None


class MovimientoCreate(BaseModel):
    producto_id: int
    tipo: Literal["entrada", "salida"]
    cantidad: int = Field(gt=0)
    motivo: str | None = None


class MovimientoRead(MovimientoCreate):
    id: int
    stock_resultante: int


PROVEEDORES: list[dict] = [
    {"id": 1, "nombre": "Distribuidora Andina", "ciudad": "Quito"},
    {"id": 2, "nombre": "Importadora del Pacífico", "ciudad": "Guayaquil"},
]

PRODUCTOS: list[dict] = [
    {
        "id": 1,
        "codigo": "HER-001",
        "nombre": "Martillo de acero",
        "categoria": "Herramientas",
        "precio": 8.50,
        "stock": 25,
        "stock_minimo": 5,
        "proveedor_id": 1,
    },
    {
        "id": 2,
        "codigo": "FIJ-010",
        "nombre": "Caja de clavos 2 pulgadas",
        "categoria": "Fijaciones",
        "precio": 3.25,
        "stock": 4,
        "stock_minimo": 10,
        "proveedor_id": 1,
    },
    {
        "id": 3,
        "codigo": "PIN-005",
        "nombre": "Pintura blanca galón",
        "categoria": "Pinturas",
        "precio": 18.75,
        "stock": 12,
        "stock_minimo": 4,
        "proveedor_id": 2,
    },
]

MOVIMIENTOS: list[dict] = []


def siguiente_id(registros: list[dict]) -> int:
    return max((registro["id"] for registro in registros), default=0) + 1


def con_alerta(producto: dict) -> dict:
    return {**producto, "stock_bajo": producto["stock"] <= producto["stock_minimo"]}


def buscar_producto(producto_id: int) -> dict:
    for producto in PRODUCTOS:
        if producto["id"] == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")


def validar_proveedor(proveedor_id: int | None) -> None:
    if proveedor_id is None:
        return
    if not any(proveedor["id"] == proveedor_id for proveedor in PROVEEDORES):
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")


@inventario_router.get("/proveedores", response_model=list[ProveedorRead])
def listar_proveedores() -> list[dict]:
    return PROVEEDORES


@inventario_router.post("/proveedores", response_model=ProveedorRead, status_code=201)
def crear_proveedor(proveedor: ProveedorCreate) -> dict:
    nuevo = {"id": siguiente_id(PROVEEDORES), **proveedor.model_dump()}
    PROVEEDORES.append(nuevo)
    return nuevo


@inventario_router.get("/productos", response_model=list[ProductoRead])
def listar_productos(categoria: str | None = None) -> list[dict]:
    productos = PRODUCTOS
    if categoria:
        productos = [p for p in PRODUCTOS if p["categoria"].lower() == categoria.lower()]
    return [con_alerta(producto) for producto in productos]


@inventario_router.get("/productos/{producto_id}", response_model=ProductoRead)
def obtener_producto(producto_id: int) -> dict:
    return con_alerta(buscar_producto(producto_id))


@inventario_router.post("/productos", response_model=ProductoRead, status_code=201)
def crear_producto(producto: ProductoCreate) -> dict:
    if any(p["codigo"] == producto.codigo for p in PRODUCTOS):
        raise HTTPException(status_code=409, detail="Ya existe un producto con ese código")
    validar_proveedor(producto.proveedor_id)
    nuevo = {"id": siguiente_id(PRODUCTOS), **producto.model_dump()}
    PRODUCTOS.append(nuevo)
    return con_alerta(nuevo)


@inventario_router.patch("/productos/{producto_id}", response_model=ProductoRead)
def actualizar_producto(producto_id: int, cambios: ProductoUpdate) -> dict:
    producto = buscar_producto(producto_id)
    datos = cambios.model_dump(exclude_unset=True)
    if "proveedor_id" in datos:
        validar_proveedor(datos["proveedor_id"])
    producto.update(datos)
    return con_alerta(producto)


@inventario_router.delete("/productos/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int) -> None:
    PRODUCTOS.remove(buscar_producto(producto_id))


@inventario_router.post("/movimientos", response_model=MovimientoRead, status_code=201)
def registrar_movimiento(movimiento: MovimientoCreate) -> dict:
    producto = buscar_producto(movimiento.producto_id)
    if movimiento.tipo == "salida":
        if movimiento.cantidad > producto["stock"]:
            raise HTTPException(
                status_code=400,
                detail=f"Stock insuficiente, solo hay {producto['stock']} unidades",
            )
        producto["stock"] -= movimiento.cantidad
    else:
        producto["stock"] += movimiento.cantidad

    nuevo = {
        "id": siguiente_id(MOVIMIENTOS),
        "stock_resultante": producto["stock"],
        **movimiento.model_dump(),
    }
    MOVIMIENTOS.append(nuevo)
    return nuevo


@inventario_router.get("/movimientos", response_model=list[MovimientoRead])
def listar_movimientos(producto_id: int | None = None) -> list[dict]:
    if producto_id is None:
        return MOVIMIENTOS
    return [m for m in MOVIMIENTOS if m["producto_id"] == producto_id]


@inventario_router.get("/alertas", response_model=list[ProductoRead])
def productos_con_stock_bajo() -> list[dict]:
    return [con_alerta(p) for p in PRODUCTOS if p["stock"] <= p["stock_minimo"]]


@inventario_router.get("/resumen")
def resumen_inventario() -> dict:
    return {
        "total_productos": len(PRODUCTOS),
        "total_unidades": sum(p["stock"] for p in PRODUCTOS),
        "valor_total": round(sum(p["stock"] * p["precio"] for p in PRODUCTOS), 2),
        "productos_stock_bajo": sum(1 for p in PRODUCTOS if p["stock"] <= p["stock_minimo"]),
    }
