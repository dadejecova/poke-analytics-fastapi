# Poke-Analytics: Full-Stack Microservices Dashboard

Este proyecto es una plataforma avanzada de análisis y visualización de Pokémon, diseñada bajo una arquitectura de microservicios y completamente contenedorizada para un despliegue ágil. Representa una solución integral que separa la lógica de negocio (Backend) de la interfaz de usuario (Frontend), garantizando escalabilidad y orden.

---

## Arquitectura del Proyecto
El proyecto ha sido reestructurado para operar en ecosistemas aislados, permitiendo que cada componente gestione sus propias dependencias de forma eficiente:

```text
poke-analytics-fastapi/
├── backend/              # Microservicio de API (FastAPI)
│   ├── app/              # Lógica, Modelos y Servicios
│   ├── Dockerfile        # Receta de construcción del Backend
│   └── requirements.txt  # Dependencias específicas de la API
├── frontend/             # Interfaz de Usuario (Streamlit)
│   ├── dashboard.py      # Visualización y Dashboard interactivo
│   ├── Dockerfile        # Receta de construcción del Frontend
│   └── requirements.txt  # Dependencias de visualización
├── docker-compose.yml    # Orquestador de contenedores
├── .gitignore            # Exclusiones de Git
└── README.md             # Documentación técnica
```
## Características Principales
- Arquitectura Desacoplada: Comunicación fluida entre servicios independientes mediante redes internas de Docker.
- Análisis Estadístico: Procesamiento de datos con Pandas y visualización avanzada con gráficos de radar en Plotly.
- Persistencia Inteligente: Almacenamiento local en SQLite mediante el ORM de SQLAlchemy para optimizar el consumo de la PokeAPI externa.
- Ready for Production: Configuración lista para ser desplegada en cualquier servidor con soporte para Docker.

## Stack
- Backend: FastAPI, Uvicorn, SQLAlchemy, httpx.
- Frontend: Streamlit, Plotly, Pandas.
- Infraestructura: Docker, Docker Compose.

## Instalación y ejecución con Docker
Para levantar todo el ecosistema (API + Dashboard) con un solo comando, asegúrate de tener Docker instalado y ejecuta:

docker-compose up --build
