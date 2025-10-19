##  Auth Service

Servicio responsable de la **autenticación y autorización** de usuarios dentro del ecosistema.  
Se encarga del registro, inicio de sesión y validación de tokens JWT para el acceso seguro a los demás servicios.

###  Funcionalidades
- Registro de nuevos usuarios  
- Inicio de sesión y validación de credenciales  
- Generación y verificación de tokens JWT  
- Middleware para proteger rutas privadas  

###  Tecnologías
- Node.js + Express  
- MongoDB o PostgreSQL  
- JWT + bcrypt  

###  Estructura
auth-service/
├── src/
│ ├── routes/
│ ├── controllers/
│ ├── models/
│ └── utils/
├── .env
└── package.json

bash
Copiar código

### ▶ Ejecución
```bash
cd auth-service
npm install
npm run start
 Puerto por defecto: 4000

 Endpoints
Método	Ruta	Descripción
POST	/auth/register	Crear un nuevo usuario
POST	/auth/login	Iniciar sesión
GET	/auth/verify	Verificar token JWT