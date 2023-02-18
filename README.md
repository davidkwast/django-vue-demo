# bdr-vue

## Requirements

* node 18.14.x
  * npm 9.5.x
* python 3.10.x
  * django 4.1.x

## Development envirenment setup

```bash

# terminal 01

cd project/front_app/frontend
nvm use 18.14
npm i 


# terminal 02

poetry install 

```

## Development runtimes

```bash


# terminal 01

cd project/front_app/frontend
npm run dev 


# terminal 02

poetry run python manage.py runserver

```

## Settings for development

```python

DEBUG = TRUE # need for "debug" template variable

INTERNAL_IPS = ['127.0.0.1'] # need for "debug" template variable

if DEBUG:
    STATICFILES_DIRS.append(
        ('src', BASE_DIR /'project'/'map_app_base'/'frontend'/'src'),
    )

```
