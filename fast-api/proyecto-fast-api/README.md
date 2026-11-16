# API Control de Inventario

API desarrollada con **FastAPI** y **uv** para gestionar el inventario de la Ferretería La Económica: productos, proveedores, entradas y salidas de stock y alertas de stock mínimo.

**Autor:** Deyvi Rivera

## Ejecución

```bash
cd fast-api/proyecto-fast-api
uv sync
uv run fastapi dev src/main.py
```

Documentación interactiva:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Estructura

```text
src/
├── main.py              # Crea la app e incluye los routers
└── routers/
    ├── hello_world.py   # Endpoints de práctica de la clase
    ├── task_router.py   # CRUD de tareas visto en clase
    └── inventario.py    # Módulo de control de inventario
```

## Endpoints de inventario

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/inventario/productos` | Lista productos, filtro opcional `?categoria=` |
| GET | `/inventario/productos/{id}` | Obtiene un producto |
| POST | `/inventario/productos` | Registra un producto |
| PATCH | `/inventario/productos/{id}` | Actualiza datos del producto (no el stock) |
| DELETE | `/inventario/productos/{id}` | Elimina un producto |
| GET | `/inventario/proveedores` | Lista proveedores |
| POST | `/inventario/proveedores` | Registra un proveedor |
| POST | `/inventario/movimientos` | Registra una entrada o salida de stock |
| GET | `/inventario/movimientos` | Historial, filtro opcional `?producto_id=` |
| GET | `/inventario/alertas` | Productos con stock igual o menor al mínimo |
| GET | `/inventario/resumen` | Total de productos, unidades y valor del inventario |

El stock solo cambia mediante movimientos, así cada entrada o salida queda registrada en el historial. Una salida mayor al stock disponible devuelve `400`.

## Ejemplo

Registrar una salida por venta:

```bash
curl -X POST http://127.0.0.1:8000/inventario/movimientos \
  -H "Content-Type: application/json" \
  -d '{"producto_id": 1, "tipo": "salida", "cantidad": 3, "motivo": "venta"}'
```

Respuesta:

```json
{
  "producto_id": 1,
  "tipo": "salida",
  "cantidad": 3,
  "motivo": "venta",
  "id": 1,
  "stock_resultante": 22
}
```
