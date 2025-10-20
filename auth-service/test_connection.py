import os
import psycopg2
import redis

POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="localhost",
        port=5432
    )
    print(" Conexión exitosa a PostgreSQL")
except Exception as e:
    print(" Error en PostgreSQL:", e)

try:
    r = redis.Redis(host="localhost", port=REDIS_PORT)
    r.ping()
    print(" Conexión exitosa a Redis")
except Exception as e:
    print(" Error en Redis:", e)

