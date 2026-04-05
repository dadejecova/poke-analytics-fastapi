# poke-analytics-fastapi

Este proyecto es una herramienta de ingeniería de datos y visualización construida con **FastAPI**. El sistema consume datos de la **PokeAPI**, los persiste en una base de datos **SQLite** mediante un ORM y realiza análisis estadísticos con **Pandas**.

---

## Arquitectura del Proyecto

```text
poke-analytics-fastapi/
├── app/
│   ├── __init__.py      # Define la carpeta como paquete Python
│   ├── main.py          # Punto de entrada y Endpoints de FastAPI
│   ├── database.py      # Configuración de conexión SQLAlchemy
│   ├── models.py        # Definición de tablas SQL (Modelos)
│   ├── schemas.py       # Esquemas de validación (Pydantic)
│   └── services.py      # Lógica de negocio y consumo de PokeAPI
├── .gitignore           # Archivos excluidos de Git (venv, .db, etc.)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación