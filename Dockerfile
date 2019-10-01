# Local development container. Includes development dependencies.
# Not to be used in production environment (yet).
FROM python:3.6

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt-get --yes update \
    && apt-get --yes upgrade \
    && pip3 install pipenv

RUN pip3 install mysqlclient
RUN pipenv install --system --deploy --dev

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
