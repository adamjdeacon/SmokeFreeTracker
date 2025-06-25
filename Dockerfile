# Use official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy only Poetry files first for caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copy project files
COPY . /app/

# Collect static files (no input prompt)
RUN python manage.py collectstatic --noinput

# Port for Cloud Run
EXPOSE 8080

# Run using Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8080"]
