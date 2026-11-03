FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY services/pipeline/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY alembic.ini alembic.ini
COPY db/ db/
COPY services/pipeline/ services/pipeline/
RUN chmod +x services/pipeline/entrypoint.sh

ENTRYPOINT ["/app/services/pipeline/entrypoint.sh"]
