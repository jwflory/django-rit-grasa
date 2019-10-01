# Local development container. Includes development dependencies.
FROM python:3.6

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt-get --yes update \
    && apt-get --yes upgrade \
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
