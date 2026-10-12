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
├── backend/          # Código fuente de FastAPI (Python)
│   ├── main.py       # Archivo principal de la API
│   ├── requirements/ # Dependencias gestionadas con uv
│   └── ...
├── frontend/         # Código fuente de Angular
│   ├── src/          # Componentes, servicios y vistas
│   └── ...
└── README.md         # Documentación del proyecto
```

## Instrucciones de Ejecución

### Backend (FastAPI con uv)
1. Navegar a la carpeta del backend: `cd backend`
2. Crear un entorno virtual y activar dependencias usando `uv`.
3. Ejecutar el servidor: `uvicorn main:app --reload`

### Frontend (Angular)
1. Navegar a la carpeta del frontend: `cd frontend`
2. Instalar dependencias: `npm install`
3. Iniciar el servidor de desarrollo: `ng serve`