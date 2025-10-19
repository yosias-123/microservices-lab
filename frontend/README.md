## Frontend

Aplicación React que actúa como interfaz principal del sistema.
Consume las APIs de los microservicios mediante el Reverse Proxy.

## Funcionalidades

Registro e inicio de sesión de usuarios

Creación y lectura de publicaciones

Edición y eliminación de contenido propio

Panel de usuario con información de perfil

## Tecnologías

React + Vite

Axios

React Router DOM

TailwindCSS

## Estructura
frontend/
 ├── src/
 │   ├── components/
 │   ├── pages/
 │   ├── services/
 │   └── App.jsx
 ├── .env
 └── package.json

## Ejecución
cd frontend
npm install
npm run dev


 Puerto por defecto: 5173

Configurar la variable VITE_API_URL en .env para apuntar al proxy.