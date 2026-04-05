# poke-analytics-fastapi

Idea de Estructura

poke-analytics-fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py          # Punto de entrada de FastAPI
│   ├── database.py      # Configuración de SQLAlchemy
│   ├── models.py        # Tablas de SQL
│   ├── schemas.py       # Validaciones de Pydantic
│   └── services.py      # Lógica para llamar a la PokeAPI
├── .gitignore
├── requirements.txt
└── README.md


---
# Creación de entorno virtual

python -m venv venv

# Teoría de arquitectura

- __init__.py: Dice a python "este es un paquete de código", permitiendo que archivos hablen entre si.
- database.py: Aquí vamos a configurar la conexión de la base
- models.py: Aquí vamos a definir las tablas
- schemas.py: aqui definimos lo que queremos recibir.
- services.py: Aquí pondremos la lógica.

# Librerias a utilizar

pip install fastapi uvicorn sqlalchemy httpx

- fastAPI: Nuestro Framework web
- Uvicorn: el servidor
- SQLAlchemy: ORM (Traductor de Python a SQL)
- Httpx: para hacer peticiones "Asíncronas"
