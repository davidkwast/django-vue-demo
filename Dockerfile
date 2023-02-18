FROM python:3.11.2-bullseye


# LINUX - runtimes, libs, python, node

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs && apt-get clean
RUN apt-get update && apt-get install -y nginx libgdal-dev && apt-get clean
RUN pip install --upgrade pip poetry virtualenv supervisor gunicorn && npm install -g npm@latest


# PYTHON - libs

WORKDIR /srv
ADD poetry.lock /srv/
ADD pyproject.toml /srv/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi


# DOCKER - container OS stuff

ADD container/ /


ADD manage.py /srv/
ADD project/ /srv/project/


WORKDIR /srv/project/front_app/frontend
RUN npm i && npm run build && rm -rf node-modules

WORKDIR /srv
RUN python manage.py collectstatic --no-input

RUN rm /srv/static/index.html


EXPOSE 80/tcp

ENTRYPOINT ["supervisord", "-c", "/srv/supervisord.conf"]

# EXPOSE 8000/tcp
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
