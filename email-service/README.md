## Email Service

Servicio que gestiona el envío de correos electrónicos y notificaciones.
Otros servicios lo utilizan para enviar mensajes automáticos a los usuarios.

## Funcionalidades

Envío de correos transaccionales

Uso de plantillas HTML

Integración con Auth y Blog Services

Registro de logs de envío

## Tecnologías

Node.js + Express

Nodemailer

dotenv + Handlebars

## Estructura
email-service/
 ├── src/
 │   ├── routes/
 │   ├── services/
 │   ├── templates/
 │   └── utils/
 ├── .env
 └── package.json

## Ejecución
cd email-service
npm install
npm run start


## Puerto por defecto: 4002

## Endpoints
Método	Ruta	Descripción
POST	/email/send	Enviar correo electrónico