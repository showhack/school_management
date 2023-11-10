# Makefile para el proyecto "school_management"

# Crea una red Docker para el proyecto
setup:
	docker network create school_management_local || true
	docker-compose -f docker-compose.local.yml build
	docker-compose -f docker-compose.local.yml run --rm web python manage.py migrate
	docker-compose -f docker-compose.local.yml run --rm web python manage.py createsuperuser

# Build de la aplicación
build:
	docker-compose -f docker-compose.local.yml build --progress=plain

# Ejecuta las migraciones
migrate:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py migrate

# Inicia la aplicación
start:
	docker-compose -f docker-compose.local.yml up --attach web

# Crea migraciones
make-migrations:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py makemigrations

# Fusiona migraciones
merge-migrations:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py makemigrations --merge

# Otros comandos
# ...

# Ejecuta tests
test:
	-docker-compose -f docker-compose.test.yml -p school_management_backend_test run --rm web pytest $(arg)
	docker-compose -f docker-compose.test.yml -p school_management_backend_test down

# Otros comandos relacionados con la base de datos
# ...

# Comando para ejecutar manage.py de Django
managepy:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py $(ARGS)

# Comando para poblar la base de datos
populate_database:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py populate_database

# Comando para sincronizar campos de traducción
sync_translation_fields:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py sync_translation_fields

# Comando para acceder a la consola de la base de datos
dbshell:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py dbshell

down:
	docker-compose -f docker-compose.local.yml down

clear-volumes:
	docker-compose -f docker-compose.local.yml down -v

startapp:
	docker-compose -f docker-compose.local.yml run --rm web python manage.py startapp $(ARGS)

release-port-postgres:
	sudo lsof -i :5432

kill-process:
	sudo kill -9 $(ARGS)