# 🌐 Reverse Proxy

Este servicio actuará como un **gateway local** que unifica el acceso a los distintos microservicios.  
El proxy se encargará de enrutar las solicitudes HTTP hacia el servicio correcto (Auth, Blog, Email, etc.).

## Funcionalidades previstas
- Redirección de peticiones según el endpoint (`/auth`, `/blog`, `/email`).
- Balanceo de carga entre servicios.
- Configuración con Nginx o Traefik.
- Servir el frontend desde un solo punto de entrada.

## Tecnologías
- Nginx (principalmente)
- Docker Compose
