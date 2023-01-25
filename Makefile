runserver:
		python3 manage.py runserver
shell:
		poetry run python3 manage.py shell_plus
secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
