FROM python:3.8-slim-buster

WORKDIR /opt/api
COPY . /opt/api

RUN pip install fastapi uvicorn sqlalchemy
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]