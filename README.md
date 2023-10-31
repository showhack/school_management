# Aplicación de Gestión Escolar (School Management)

Bienvenido a la Aplicación de Gestión Escolar (school_management). Esta aplicación está diseñada para ayudar a administrar y supervisar las operaciones diarias en una escuela. Proporciona funciones clave para la gestión de estudiantes, profesores, cursos y más.

## Requisitos

Asegúrate de tener instalados los siguientes requisitos antes de configurar y ejecutar la aplicación:

- Python 3.8 o superior
- PostgreSQL (base de datos)
- Docker y Docker Compose (opcional, para desarrollo)

## Configuración

### Instalación de Docker en Ubuntu

Docker es una plataforma de contenedores que simplifica el despliegue de aplicaciones en contenedores. A continuación, se detallan los pasos para instalar Docker en Ubuntu.

### Pasos:

1. **Actualiza el índice de paquetes**:

   Abre una terminal y actualiza el índice de paquetes para asegurarte de que dispones de la información más reciente sobre los paquetes disponibles:

   ```bash
   sudo apt update
   ```

2. **Instala las dependencias**:

   Asegúrate de que tienes las dependencias necesarias para que APT pueda usar paquetes sobre HTTPS:

   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

3. **Agrega la clave GPG de Docker**:

   Descarga la clave GPG oficial de Docker para verificar la integridad de los paquetes:

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. **Agrega el repositorio de Docker**:

   Agrega el repositorio de Docker a tu sistema:

   ```bash
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. **Instala Docker Engine**:

   Actualiza nuevamente el índice de paquetes y luego instala Docker:

   ```bash
   sudo apt update
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

6. **Verifica la instalación**:

   Verifica que Docker se haya instalado correctamente ejecutando:

   ```bash
   sudo docker --version
   ```

   Deberías ver la versión de Docker instalada.

## Instalación de Docker Compose en Ubuntu

Docker Compose es una herramienta para definir y ejecutar aplicaciones Docker en contenedores. A continuación, se detallan los pasos para instalar Docker Compose en Ubuntu.

### Pasos:

1. **Descarga Docker Compose**:

   Descarga la última versión estable de Docker Compose desde el repositorio oficial de GitHub. Asegúrate de consultar la página de lanzamientos para obtener la URL de descarga correcta:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

2. **Concede permisos de ejecución**:

   Concede permisos de ejecución al binario de Docker Compose:

   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

3. **Verifica la instalación**:

   Verifica que Docker Compose se haya instalado correctamente ejecutando:

   ```bash
   docker-compose --version
   ```

   Deberías ver la versión de Docker Compose instalada.

Ahora tienes Docker y Docker Compose instalados en tu sistema Ubuntu. Puedes utilizar estas herramientas para gestionar contenedores y desplegar aplicaciones de manera eficiente.

Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno de desarrollo:

1. Clona este repositorio:

   ```bash
   git clone https://tu-repositorio.git
   cd school_management
   ```

2. Crea un archivo `.env` en la raíz del proyecto y copia el contenido del archivo `.env.example` en él. Asegúrate de configurar las variables de entorno necesarias en el archivo `.env`.

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

```

Asegúrate de que el archivo `.env` se crea y configura correctamente antes de ejecutar la aplicación. También, si deseas proporcionar información adicional sobre cómo instalar Docker y Docker Compose, puedes agregarlo en la sección de requisitos o en una sección separada en el README.
