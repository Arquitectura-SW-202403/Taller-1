# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requirements a la imagen
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación a la imagen
COPY . .

# Exponer los puertos para cada servicio
EXPOSE 5002

# Comando predeterminado para ejecutar el productor y los consumidores
CMD ["sh", "-c", "python bid_analytics.py"]
