# Define variables
CD_APP = cd app &&
MANAGE = $(CD_APP) python manage.py

# Define targets and recipes
.PHONY: run migrate superuser app shell


run:
	$(CD_APP) gunicorn -c .gunicorn/gunicorn.local.py app.wsgi:application --reload

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

app:
	@read -p "Enter the app name: " app_name; \
	$(MANAGE) startapp $$app_name

shell:
	$(MANAGE) shell_plus

urls:
	$(MANAGE) show_urls
