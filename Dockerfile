# Usamos una imagen ligera de Python 3.11
FROM python:3.11-slim

WORKDIR /app

# Instalación de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia de la aplicación
COPY . .

# Exponemos el puerto 8080 (estándar de Cloud Run)
EXPOSE 8080

CMD ["python", "main.py"]