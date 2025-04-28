FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py agents.yaml /app/

CMD ["python3", "main.py"]
