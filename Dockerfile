FROM python:3.10.3-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py", "5"]
