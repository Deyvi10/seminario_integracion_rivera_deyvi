# Seminario de Integración - Proyecto Final

**Institución:** Universidad UTE

**Materia:** Seminario de Integración

## Datos del Estudiante

* **Nombre:**  Deyvi Rivera
* **Carrera:**  Desarrollo de Software 
* **Nivel/Semestre:**  4to Semestre
* **Docente:**  Francisco Higeras
* **Fecha:** Octubre 2026

## Descripción del Proyecto

Este repositorio contiene el código desarrollado durante la materia de **Seminario de Integración**. El objetivo principal es consolidar los conocimientos adquiridos mediante la creación de un proyecto full-stack moderno, integrando tecnologías de backend y frontend de alto rendimiento.

## Giro de Negocio: Control de Inventario

El mini proyecto aplica cada tema de la materia a un **sistema de control de inventario** para una ferretería (*Ferretería La Económica*). El sistema cubre:

* **Productos:** registro, consulta, actualización y eliminación con código, categoría, precio y proveedor.
* **Stock:** cantidad disponible por producto y valor total del inventario.
* **Entradas y salidas:** movimientos que suben o bajan el stock y quedan en un historial.
* **Proveedores:** registro de los proveedores que abastecen cada producto.
* **Alertas de stock mínimo:** aviso cuando un producto llega o baja de su stock mínimo para generar el pedido de reposición.

Cada ejercicio de clase tiene su versión aplicada al inventario en el archivo con sufijo `_mp` (mini proyecto).

| Tema | Ejercicio de clase | Mini proyecto de inventario |
|------|--------------------|-----------------------------|
| Hola mundo | `01_hello_world.py` | `01_hello_world_mp.py` |
| Variables | `02_variables.py` | `02_variables_mp.py` |
| Input y conversiones | `03_input.py` | `03_input_mp.py` |
| Operadores | `04_operadores.py` | `04_operadores_mp.py` |
| Condicionales | `05_condicional.py` | `05_condicional_mp.py` |
| Strings | `06_strings.py` | `06_strings_mp.py` |
| Colecciones | `07_colecciones.py` | `07_colecciones_mp.py` |
| CRUD con listas | `08_crud_listas.py` | `08_crud_listas_mp.py` |
| Ciclo for | `09_ciclo_for.py` | `09_ciclo_for_mp.py` |
| Ciclo while | `10_ciclo_while.py` | `10_ciclo_while_mp.py` |
| Funciones | `11_funciones.py` | `11_funciones_mp.py` |
| POO: clases | `12_poo_clase.py` | `12_poo_clase_mp.py` |
| POO: encapsulamiento | `13_poo_encapsulamiento.py` | `13_poo_encapsulamiento_mp.py` |
| POO: herencia | `14_poo_herencia.py` | `14_poo_herencia_mp.py` |
| POO: polimorfismo | `15_polimorfismo.py` | `15_polimorfismo_mp.py` |
| POO: clase abstracta | `16_clase_abstracta.py` | `16_clase_abstracta_mp.py` |

## Tecnologías Utilizadas

A continuación, se describen las tecnologías principales empleadas en la arquitectura de este proyecto:

### 🐍 Python
Es un lenguaje de programación de propósito general, de alto nivel y muy versátil. En este proyecto se utiliza como base para el desarrollo de la lógica del servidor (backend), destacando por su legibilidad y eficiencia en la integración de sistemas.

### ⚡ uv
Es un gestor de paquetes y proyectos para Python extremadamente rápido, escrito en Rust. Sirve como un reemplazo moderno y eficiente para herramientas como `pip`, `pip-tools` o `virtualenv`, reduciendo significativamente los tiempos de resolución e instalación de dependencias.

### 🚀 FastAPI
Es un framework web moderno y de alto rendimiento para construir APIs (Interfaces de Programación de Aplicaciones) con Python. Basado en las anotaciones de tipos estándar de Python, permite crear endpoints rápidos, con validación de datos automática y documentación interactiva autogenerada (Swagger/ReDoc).

### 🅰️ Angular
Es un framework y plataforma de desarrollo frontend creado por Google. Utilizado para construir aplicaciones web de una sola página (SPA - *Single Page Applications*), Angular utiliza TypeScript y HTML para crear interfaces de usuario dinámicas, modulares y altamente escalables.

## Estructura del Proyecto

```text
/
├── python/                    # Ejercicios de clase y mini proyecto (_mp)
├── fast-api/
│   └── proyecto-fast-api/     # API de control de inventario (FastAPI + uv)
│       ├── src/main.py
│       └── src/routers/
└── README.md
```

## Ramas de Trabajo

| Rama | Contenido |
|------|-----------|
| `FEATURE-2026-2-02-PYTHON-FUNDAMENTALS` | Hola mundo, variables, input, operadores y condicionales |
| `FEATURE-2026-2-03-PYTHON-FUNDAMENTALS-LIST` | Strings, colecciones y CRUD con listas |
| `FEATURE-2026-2-04-POO` | Ciclos, funciones, clases y encapsulamiento |
| `FEATURE-2026-2-06-POO-FUNDAMENTALS` | Herencia, polimorfismo y clase abstracta |
| `FEATURE-2026-2-07-FAST-API` | API de control de inventario con FastAPI |

## Instrucciones de Ejecución

### Ejercicios de Python
```bash
cd python
python3 08_crud_listas_mp.py
```

### Backend (FastAPI con uv)
```bash
cd fast-api/proyecto-fast-api
uv sync
uv run fastapi dev src/main.py
```

La documentación de la API queda disponible en `http://127.0.0.1:8000/docs`. El detalle de los endpoints está en [fast-api/proyecto-fast-api/README.md](fast-api/proyecto-fast-api/README.md).

### Frontend (Angular)
Pendiente para las siguientes unidades de la materia.