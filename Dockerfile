ARG PYTHON_VERSION=3.9.6

FROM node:20 as frontend

RUN mkdir /static

WORKDIR /static

COPY static/package.json .

RUN npm install

# ----------

FROM python:${PYTHON_VERSION} as backend

LABEL maintainer="2023 MyHomeworks, { }"

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/static

RUN rm -rf node_modules && \ 
    mkdir node_modules

WORKDIR /app/static/node_modules

COPY --from=frontend /static/node_modules .

WORKDIR /app