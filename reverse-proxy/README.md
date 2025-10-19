## Reverse Proxy

El Reverse Proxy actúa como punto de entrada unificado del sistema.
Redirige las peticiones a los microservicios correctos, maneja CORS y agrega una capa de seguridad adicional.

## Funcionalidades

Enrutamiento hacia los servicios internos

Balanceo de carga básico

Manejo de CORS y HTTPS

Logs de tráfico

## Tecnologías

NGINX o Express Gateway

## Estructura
reverse-proxy/
 ├── nginx.conf
 ├── Dockerfile
 └── README.md

## Ejecución
cd reverse-proxy
nginx -c ./nginx.conf

## Configuración ejemplo (nginx.conf)
location /api/auth/ {
    proxy_pass http://localhost:4000/;
}
location /api/posts/ {
    proxy_pass http://localhost:4001/;
}
location /api/email/ {
    proxy_pass http://localhost:4002/;
}

## Puertos por defecto
Servicio	Puerto
Auth Service	4000
Blog Service	4001
Email Service	4002
Frontend	5173
Reverse Proxy	8080