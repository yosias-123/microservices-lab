# Microservices Lab
Laboratorio de microservicios con **Django + React**, usando Docker, PostgreSQL y Redis.

---

## 🏗 Arquitectura del proyecto

El proyecto se organiza en microservicios independientes:

- **auth-service/** → Autenticación de usuarios con JWT  
- **blog-service/** → Publicaciones, autores y categorías  
- **email-service/** → Envío de notificaciones y formularios  
- **frontend/** → Interfaz web desarrollada con React  
- **reverse-proxy/** → Proxy inverso para balanceo de carga  

### 🧩 Servicios de soporte
- **PostgreSQL** (puerto `5432`) → Base de datos principal  
- **Redis** (puerto `6379`) → Cache y sesiones  

---

## 🧪 Mini-reto del día 2 — Backend Auth

### 🎯 Objetivo
Construir un microservicio de autenticación independiente que gestione usuarios, login y tokens JWT, corriendo en su propio contenedor Docker y conectado a PostgreSQL y Redis.

### 🧩 Conceptos clave
- Autenticación basada en **JWT**  
- Servicios Django aislados  
- Variables de entorno y dependencias  
- Cacheo y sesiones con Redis  
- Comunicación segura vía API entre servicios  

### 🕐 Video de referencia
🎥 [Microservicios con Django REST Framework, Next.js y Apache Kafka](https://www.youtube.com/watch?v=wj766sxHZrM)  
📍 Desde minuto 26:13 hasta 2:54:00  
> Solo implementar REST y Redis. No implementar Kafka Producer.

---

### ⚙️ Pasos del ejercicio

#### 1️⃣ Crear proyecto Django y app `users`
```bash
cd auth-service
django-admin startproject auth_service .
python manage.py startapp users

## 2️⃣ Configurar Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]

## 3️⃣ Extender docker-compose.yml
auth:
  build: ./auth-service
  container_name: auth_service
  restart: always
  environment:
    - DEBUG=1
    - DB_HOST=postgres
    - DB_NAME=main_db
    - DB_USER=devuser
    - DB_PASS=devpass
    - REDIS_HOST=redis
    - REDIS_PORT=6379
  depends_on:
    - postgres
    - redis
  ports:
    - "8000:8000"

## 4️⃣ Instalar dependencias (requirements.txt)
django==5.0
djangorestframework==3.15
djangorestframework-simplejwt==5.3
psycopg2-binary
redis
django-cors-headers

## 5️⃣ Configurar settings.py

Añadir apps: rest_framework, corsheaders, users

Configurar DATABASES con variables de entorno

Configurar CACHES para Redis

Añadir middleware corsheaders.middleware.CorsMiddleware

Configurar REST_FRAMEWORK con JWTAuthentication

## 6️⃣ Modelo de usuario personalizado (users/models.py)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email obligatorio")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


Registrar en settings.py:

AUTH_USER_MODEL = 'users.User'

## 7️⃣ Endpoints con JWT

Usar TokenObtainPairView y TokenRefreshView de rest_framework_simplejwt

Rutas:

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/register/', RegisterView.as_view()),
]

## 8️⃣ Probar con Postman

POST /api/register/ → crear usuario

POST /api/token/ → obtener access/refresh token

POST /api/token/refresh/ → renovar token

## 9️⃣ Verificar conexión con DB y Redis
docker exec -it auth_service python manage.py shell

✅ Checklist general

 Estructura de carpetas base creada

 Git y GitHub configurados

 Docker Compose funcional

 README documentado

 Microservicio Auth levantado y probado con JWT
