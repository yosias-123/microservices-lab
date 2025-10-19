## Blog Service

Servicio encargado de la gestión de publicaciones, autores y comentarios.
Depende del Auth Service para validar la identidad de los usuarios.

## Funcionalidades

CRUD de publicaciones

Comentarios y etiquetas

Búsqueda y filtrado

Validación JWT con Auth Service

## Tecnologías

Node.js + Express

MongoDB

Axios + JWT

## Estructura
blog-service/
 ├── src/
 │   ├── routes/
 │   ├── controllers/
 │   ├── models/
 │   └── middleware/
 ├── .env
 └── package.json

## Ejecución
cd blog-service
npm install
npm run start


 Puerto por defecto: 4001

## Endpoints
Método	Ruta	Descripción
GET	/posts	Listar publicaciones
POST	/posts	Crear nueva publicación
PUT	/posts/:id	Actualizar publicación
DELETE	/posts/:id	Eliminar publicación