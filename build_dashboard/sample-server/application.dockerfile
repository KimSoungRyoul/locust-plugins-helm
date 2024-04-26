FROM python:3.12-slim

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./main.py main.py

ENTRYPOINT ["uvicorn", "main:app", "--workers", "3", "--host", "0.0.0.0", "--port", "8000"]
