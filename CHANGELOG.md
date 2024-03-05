# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changes

* argon2-cffi for password hashing
* whitenoise for serving static files
* gunicorn instead of `manage.py runserver`
* debugpy using `manage.py runserver_plus 5678`

### Added

* postgres database mounted to a named volume
* django-debug-toolbar
* django-cors-headers
* pylint
* ruff
