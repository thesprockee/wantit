runserver: collectstatic
	@python manage.py runserver_plus 0.0.0.0:8000

collectstatic:
	@yes yes | python manage.py collectstatic -l
