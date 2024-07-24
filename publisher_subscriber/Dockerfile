# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos del directorio actual al contenedor
COPY . /app

# Instala las dependencias
RUN pip install pika

# Comando por defecto para ejecutar el script
CMD ["sh", "-c", "python bid_producer.py & python bid_consumer_capture.py & python bid_consumer_analytics.py & python bid_consumer_tracking.py"]
