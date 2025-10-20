# microservices-lab
# Laboratorio de Microservicios (Django + React)

##  Arquitectura inicial

- **auth-service/** → Autenticación y tokens JWT  
- **blog-service/** → Publicaciones, autores y categorías  
- **email-service/** → Notificaciones y formularios  
- **frontend/** → Interfaz React  
- **reverse-proxy/** → Balanceo / Gateway local  

###  Servicios base
- PostgreSQL (5432)
- Redis (6379)

##  Mini-reto del día
1. Levantar los contenedores (`docker compose up -d`)
2. Crear `auth-service/test_connection.py` para probar conexión a PostgreSQL y Redis.
3. Ejecutarlo dentro del contenedor (`docker exec -it ...`)

##  Checklist
- [x] Estructura base creada
- [x] Git y GitHub configurados
- [x] Docker Compose funcional
- [x] README documentado
