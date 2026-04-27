# Usamos una versión oficial y ligera de Python
FROM python:3.12-slim

# Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos solo los requerimientos primero (para aprovechar el caché de Docker)
COPY requirements.txt .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código (la carpeta app)
COPY . .

# Exponemos el puerto de FastAPI
EXPOSE 8000

# El comando para prender la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]