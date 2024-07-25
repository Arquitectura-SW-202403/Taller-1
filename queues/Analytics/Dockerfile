# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Comando predeterminado para ejecutar el productor y los consumidores
CMD ["python", "-u", "bid_consumer_analytics.py"]
