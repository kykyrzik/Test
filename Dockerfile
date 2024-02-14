FROM python:3.10.13-alpine3.19

WORKDIR /usr/src/project
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY . .
WORKDIR /usr/src/project/
RUN pip install -r requirements.txt