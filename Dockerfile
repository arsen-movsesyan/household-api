FROM python:3.11-slim
LABEL authors="arsen_movsesyan"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER Yes
ENV PYTHONPATH .
ENV DJANGO_SETTINGS_MODULE household.settings

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client

COPY requirements.txt /opt

WORKDIR /opt
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY .. .

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
