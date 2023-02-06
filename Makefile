LOCAL := poetry run python manage.py

install:
		poetry install

# runserver commands
runserver:
		$(LOCAL) runserver localhost:8080
run-gunicorn:
		export DJANGO_SETTINGS_MODULE=ndt_manager.settings
		poetry run gunicorn ndt_manager.wsgi --log-file -

# service commands
shell:
		$(LOCAL) shell_plus
secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

# make translate messages commands
messages:
		poetry run django-admin makemessages -l ru
compilemess:
		poetry run django-admin compilemessages

# migrate commands
migrations:
		$(LOCAL) makemigrations ndt_manager equipment users stations equiptypes reports certificates
migrate:
		$(LOCAL) migrate
migrate-rw:
		railway run python manage.py migrate
		pgloader db.sqlite3 postgresql://postgres:6LGDDkAme42r1Ol2c0Wd@containers-us-west-188.railway.app:6064/railway

# test commands
test:
		poetry run pytest
test-cov:
		poetry run pytest --cov
test-coverage:
		poetry run pytest --cov=task_manager --cov-report xml

# linter & check commands
lint:
		poetry run flake8 ndt_manager users stations equipment equiptypes reports certificates

selfcheck:
		poetry check

# complex commands
check: selfcheck test lint

build: check
		poetry build

.PHONY: install test lint selfcheck check build shell migrate collectstatic secretkey