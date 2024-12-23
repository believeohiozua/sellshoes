FROM python:3.10.14-alpine3.20 as base

RUN apk update && apk add --no-cache \
    bash \
    curl \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    libffi-dev \
    openssl-dev 

RUN addgroup -S mygroup && adduser -S -G mygroup myuser

USER $USER

RUN python -m venv /venv

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/pybay-venv 
ENV \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.8.4

RUN python -m venv /$VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /sellshoes/app

COPY ./sellshoes/ .

RUN python -m venv $VIRTUAL_ENV \
    && . $VIRTUAL_ENV/bin/activate \
    && pip install --upgrade pip setuptools wheel poetry==$POETRY_VERSION \
    && poetry install --no-root

EXPOSE 8000

FROM base as api-prod

CMD ["poetry", "run", "python", "manage.py", "makemigrations", "--noinput"]