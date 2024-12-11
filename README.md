
# Guía de Clonación y Despliegue del Proyecto

Este documento proporciona los pasos necesarios para clonar y desplegar tanto el backend como el frontend del proyecto.

## Requisitos Previos

- Tener **Git** instalado en tu máquina.
- Tener **Node.js** y **npm** instalados para el frontend.
- Tener **Python** y **Django** instalados para el backend.
- Tener **PostgreSQL** o cualquier otra base de datos configurada para el backend (si se requiere).

### Backend (Django)

1. **Clonar el Repositorio:**
   Abre una terminal y clona el repositorio del backend:
   
   ```bash
   git clone https://github.com/tu_usuario/backend-repository.git
   ```

2. **Crear un Entorno Virtual:**
   Entra en la carpeta del proyecto backend y crea un entorno virtual para gestionar las dependencias de Python.

   ```bash
   cd backend-repository
   python -m venv venv
   source venv/bin/activate  # En Linux o Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar las Dependencias:**
   Instala las dependencias de Python que se encuentran en el archivo `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos:**
   Si estás usando PostgreSQL u otra base de datos, asegúrate de configurarla en el archivo `settings.py`. Asegúrate de tener creada la base de datos.

5. **Realizar las Migraciones:**
   Ejecuta las migraciones para crear las tablas en la base de datos.

   ```bash
   python manage.py migrate
   ```

6. **Crear un Superusuario:**
   Si necesitas acceso a la interfaz de administración de Django, crea un superusuario.

   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar el Servidor:**
   Inicia el servidor de desarrollo de Django.

   ```bash
   python manage.py runserver
   ```

   El servidor debería estar corriendo en `http://127.0.0.1:8000/`.
