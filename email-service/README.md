# 📧 Email Service

Servicio encargado del **envío de correos electrónicos** dentro del ecosistema.  
Permitirá enviar notificaciones automáticas a los usuarios, por ejemplo, al registrarse o publicar contenido.

## Funcionalidades previstas
- Envío de correos de confirmación o recuperación de contraseña.
- Notificaciones automáticas por nuevas publicaciones o eventos.
- Integración con otros servicios mediante colas o eventos (RabbitMQ o Redis Pub/Sub).

## Tecnologías
- Python + Celery
- Redis (como broker de tareas)
- Servicio SMTP externo (Gmail, Mailtrap, etc.)
