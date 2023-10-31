# Utiliza la imagen oficial de Python como base
FROM python:3.10

# Establece variables de entorno
ENV PYTHONUNBUFFERED 1

ENV CFLAGS="$CFLAGS -L/lib"

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y libpq-dev && apt-get install -y libgdal-dev

RUN apt-get update \
  && apt-get install -y libgdal-dev python3-gdal libgeos-dev libproj-dev

# Crea un directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo Pipfile y Pipfile.lock al contenedor
COPY Pipfile /app/
COPY Pipfile.lock /app/

# Instala pipenv en el contenedor
RUN pip install pipenv

# Instala las dependencias del proyecto usando pipenv
RUN pipenv install --deploy

RUN pipenv install --dev --system
WORKDIR /
RUN rm -rf /app/Pipfile \
  && rm -rf /app/Pipfile.lock

# Copia el código de tu aplicación al contenedor
COPY . /app/

COPY ./compose/local/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
# Puerto en el que se ejecutará tu aplicación (ajústalo según tus necesidades)
EXPOSE 8000

WORKDIR /app
ENTRYPOINT ["/entrypoint"]
