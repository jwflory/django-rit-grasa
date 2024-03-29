# Local development container.
# Includes development dependencies. Django runs with development settings.
FROM python:3.9-bullseye

ENV DJANGO_SETTINGS_MODULE=grasa_event_locator.settings.development

RUN mkdir /app
WORKDIR /app
COPY Pipfile /app
COPY Pipfile.lock /app

RUN apt-get --yes update \
    && apt-get --yes upgrade \
    && pip3 install pipenv

RUN pipenv install --system --deploy --dev

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
