# Servicio de Autenticación (auth-service)

Este servicio se encarga de la autenticación de usuarios y la generación/validación de tokens JWT. Es un componente fundamental del backend, construido con Django.

## Tecnologías
- Python
- Django
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL (como base de datos)
- Redis (para caching/sesiones)

## Configuración y Ejecución (Desarrollo Local)
Para ejecutar este servicio localmente:
1.  Asegúrate de tener Python y pip instalados.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Configura las variables de entorno necesarias (puedes ver un ejemplo en el `.env.example` de la raíz del proyecto).
