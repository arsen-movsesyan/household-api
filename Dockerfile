FROM python:3.9.4-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER Yes

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENV PYTHONPATH .
ENV DJANGO_SETTINGS_MODULE household.settings

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
