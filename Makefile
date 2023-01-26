runserver:
		python3 manage.py runserver localhost:8080
runserver3000:
		python3 manage.py runserver 0.0.0.0:3000
migrations:
		python3 manage.py makemigrations ndt_manager, equipment, users
migrate:
		python3 manage.py migrate
shell:
		poetry run python3 manage.py shell_plus
secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
