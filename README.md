# 🧪 Laboratorio de Microservicios (Django + React)

Este proyecto es un entorno de práctica para aprender microservicios utilizando Django (backend), React (frontend), y Docker Compose como herramienta de orquestación.

---

## ⚙️ Arquitectura inicial

**Servicios principales:**
- **auth-service/** → Servicio de autenticación (usuarios, login, JWT)
- **blog-service/** → Servicio de publicaciones, autores y categorías
- **email-service/** → Servicio de notificaciones y envío de correos
- **frontend/** → Interfaz React para consumir los microservicios
- **reverse-proxy/** → Gateway local (Nginx o Traefik para enrutar peticiones)

**Servicios base (en Docker Compose):**
- **PostgreSQL** → Base de datos principal (puerto `5432`)
- **Redis** → Sistema de cache y colas (puerto `6379`)

---

## 📂 Estructura del proyecto

microservices-lab/
│
├── auth-service/
├── blog-service/
├── email-service/
├── frontend/
├── reverse-proxy/
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md


---

## 🚀 Iniciar entorno base

```bash
docker compose up -d
docker ps

Si ves los contenedores db_postgres y cache_redis activos ✅, el entorno base está listo.