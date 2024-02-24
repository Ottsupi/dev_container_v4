# Django API project template

DRF template configured for **VS Code Dev Container**

## Features

* Gunicorn 21.2
* Django 4.2
* Django Rest Framework 3.14
* Postgres 15
* Whitenoise

## Setup

1. Create a folder
2. Git clone and delete `.git` folder

        git clone https://github.com/Ottsupi/dev_container_v3.git .
        rm -rf .git

3. Generate your own secret key
4. Configure environment variables at `.env/` folder
5. Rename Dev Container at `.devcontainer.json`
6. Open VS Code and reopen in Dev Container

## Packages

* django-model-utils
* django-pghistory
* django-cors-headers

### For Local Development

* django-debug-toolbar
