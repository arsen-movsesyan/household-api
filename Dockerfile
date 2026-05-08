FROM python:3.14-slim
LABEL authors="arsen_movsesyan"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

RUN python manage.py collectstatic --noinput 2>/dev/null || true
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
