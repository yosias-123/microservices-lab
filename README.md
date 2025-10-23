# 🧩 microservices-lab  
**Laboratorio de Microservicios con Django, PostgreSQL, Redis y Docker Compose**

---

## 🚀 Descripción general

Este proyecto implementa una arquitectura de **microservicios** utilizando **Django REST Framework** para la capa backend, **PostgreSQL** como base de datos principal, y **Redis** para manejo de cache y sesiones.  
Cada servicio es independiente, desplegable en contenedores con **Docker Compose**, y se comunica a través de endpoints REST.

Actualmente, el módulo **`auth-service`** se encuentra completamente funcional con autenticación JWT.

---

## 🏗️ Estructura del proyecto

microservices-lab/
│
├── auth-service/ # Servicio de autenticación (Django + DRF + JWT)
│ ├── users/ # App interna para gestión de usuarios
│ ├── auth_service/ # Configuración principal del servicio
│ ├── Dockerfile
│ ├── requirements.txt
│ └── manage.py
│
├── blog-service/ # Servicio de publicaciones (pendiente)
├── email-service/ # Servicio de notificaciones (pendiente)
├── frontend/ # Interfaz en React (pendiente)
├── reverse-proxy/ # Proxy Nginx para enrutar microservicios
│
├── docker-compose.yml # Orquestador de todos los contenedores
├── .env.example # Variables de entorno base
└── README.md

---

## ⚙️ Servicios principales

| Servicio | Descripción | Puerto |
|-----------|--------------|--------|
| **auth-service** | Django + DRF + SimpleJWT (autenticación) | `8000` |
| **db_postgres** | Base de datos PostgreSQL | `5432` |
| **cache_redis** | Sistema de cache Redis | `6379` |
| **frontend** | Interfaz React | `3000` |
| **reverse-proxy** | Nginx Gateway local | `80` |

---

## 🔐 Endpoints del Auth Service

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| `POST` | `/api/register/` | Registrar nuevo usuario |
| `POST` | `/api/token/` | Obtener tokens JWT (`access` y `refresh`) |
| `POST` | `/api/token/refresh/` | Renovar token de acceso |
| `GET` | `/api/me/` | Ver información del usuario autenticado |

📌 **Nota:** El endpoint `/api/me/` requiere autenticación.  
Debes incluir en los encabezados:


---

## 🧪 Mini-reto técnico

### 1️⃣ Levantar los contenedores
```bash
docker compose up -d
docker ps
docker exec -it auth_service python manage.py shell

🧰 Tecnologías utilizadas

Python 3.12
Django 5.0
Django REST Framework 3.15
Simple JWT 5.3
PostgreSQL
Redis
Docker & Docker Compose
Nginx (Reverse Proxy)

📄 Archivo requirements.txt
django==5.0
djangorestframework==3.15
djangorestframework-simplejwt==5.3
psycopg2-binary
redis
django-cors-headers

✅ Checklist de avance
 Configuración base del proyecto
 Docker Compose funcional
 Conexión con PostgreSQL y Redis
 Auth Service operativo
 Endpoint /api/me/ implementado
 Pruebas con Postman exitosas
 Documentación inicial (README)
