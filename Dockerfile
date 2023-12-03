FROM python:3.11.6-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get upgrade
RUN python -m pip install --upgrade pip
RUN pip install poetry

COPY . .
RUN poetry install

CMD ["python", "main.py"]
