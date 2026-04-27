# Usamos la misma versión de Python
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el dashboard.py
COPY . .

# Exponemos el puerto de Streamlit
EXPOSE 8501

# El comando para prender el Dashboard
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]