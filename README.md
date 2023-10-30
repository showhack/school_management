# School Management Application

Bienvenido a la aplicación de gestión escolar (school_management). Esta aplicación está diseñada para ayudar a administrar y supervisar las operaciones diarias en una escuela. Proporciona funciones clave para la gestión de estudiantes, profesores, cursos y más.

## Requisitos

- Python 3.8 o superior
- PostgreSQL (base de datos)
- Docker y Docker Compose (opcional, para desarrollo)

## Configuración

A continuación, se describen los pasos para configurar y ejecutar la aplicación en tu entorno de desarrollo:

1. Clona este repositorio:

   ```bash
   git clone https://tu-repositorio.git
   cd school_management
   ```

La aplicación estará disponible en [http://localhost:8000/](http://localhost:8000/).

## Comandos Útiles

Puedes utilizar los siguientes comandos para administrar la aplicación:

- **Configurar el Entorno y Migrar la Base de Datos**:
  ```bash
  make setup
  ```

- **Crear Migraciones**:
  ```bash
  make make-migrations
  ```

- **Fusionar Migraciones**:
  ```bash
  make migrate
  ```

- **Iniciar el Servidor de Desarrollo**:
  ```bash
  make start
  ```

- **Otros Comandos Útiles**:
  Consulta el archivo Makefile para más comandos relacionados con la base de datos, pruebas y administración.

## Uso

La aplicación proporciona una interfaz web para administrar estudiantes, profesores, cursos y otros aspectos de la gestión escolar. Puedes acceder a la interfaz de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/) con las credenciales de superusuario.

## Contribuciones

Si deseas contribuir a este proyecto, ¡estamos abiertos a colaboraciones! Siéntete libre de crear un fork y enviar tus solicitudes de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

¡Esperamos que disfrutes utilizando la aplicación "school_management"! Si tienes alguna pregunta o necesitas asistencia, no dudes en ponerte en contacto con nosotros.
