import os # Funciones para interactuar con el entorno (archivos, carpetas, etc)
import psycopg2 # Herramientras para conectar y hablar con base de datos PostgreSQL
import redis # Herramienta para conectar y verificar la conexion a servidores de Redis 
import time # Funciones relacionadas a la hora y medicion en lapsos
import sys # Se usa principalmente para indicar si el script terminó con éxito o con error

def check_postgres():
    try:
        print("Intentando conectar a PostgreSQL...")
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=5432
        )
        conn.close()
        print("Conexión a PostgreSQL exitosa.\n")
        return True
    except Exception as e:
        print(f"ERROR: No se pudo conectar a PostgreSQL.")
        print(f"   Detalle: {e}\n")
        return False

def check_redis():
    try:
        print("Intentando conectar a Redis...")
        r = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=os.getenv("REDIS_PORT"),
            db=0,
            socket_connect_timeout=2 # Pequeño tiempo de espera
        )
        r.ping()
        print("Conexión a Redis exitosa.\n")
        return True
    except Exception as e:
        print(f"   ERROR: No se pudo conectar a Redis.")
        print(f"   Detalle: {e}\n")
        return False

if __name__ == "__main__":
    print("--- Iniciando verificación de servicios Docker ---\n")
    
    # Bucle para reintentar, aveces los servicios tardan en correr
    max_retries = 5
    retries = 0
    services_ready = False

    while retries < max_retries and not services_ready:
        if retries > 0:
            print(f"--- Reintentando en 5 segundos... (Intento {retries + 1}/{max_retries}) ---\n")
            time.sleep(5)
        
        postgres_ok = check_postgres()
        redis_ok = check_redis()

        if postgres_ok and redis_ok:
            services_ready = True
        
        retries += 1

    # Dependientemente de si la conexión haya sido correcta o no, se mostrará el siguiente 
    print("--- Verificación finalizada ---")
    if services_ready:
        print("¡Todos los servicios están conectados y funcionando correctamente!")
        sys.exit(0) # Exito
    else:
        print("¡Uno o más servicios no están respondiendo! Revisa los logs de Docker.")
        sys.exit(1) # Error