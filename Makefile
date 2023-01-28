LOCAL := poetry run python manage.py

install:
		poetry install

# runserver commands
runserver:
		$(LOCAL) runserver localhost:8080
runserver3000:
		$(LOCAL) runserver 0.0.0.0:3000

# service commands
shell:
		$(LOCAL) shell_plus
secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

# migrate commands
migrations:
		$(LOCAL) makemigrations ndt_manager equipment users stations equiptypes
migrate:
		$(LOCAL) migrate
migrate-rw:
		railway run python manage.py migrate

# test commands
test:
		poetry run pytest
test-cov:
		poetry run pytest --cov
test-coverage:
		poetry run pytest --cov=task_manager --cov-report xml

# linter & check commands
lint:
		poetry run flake8 ndt_manager users stations equipment equiptypes

selfcheck:
		poetry check

# complex commands
check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build shell migrate collectstatic secretkey