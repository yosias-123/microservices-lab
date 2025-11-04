FROM python:3.11-slim

# Evita mensajes interactivos de apt-get
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copia primero requirements para aprovechar cache
COPY requirements.txt /app/

# Instala dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia el resto del proyecto
COPY . /app

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
