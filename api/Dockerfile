FROM python:3.8-slim-buster

RUN mkdir -p /opt/api
COPY . /opt/api
COPY hackathon.db /opt/hackathon.db

ENV SQLITE_PATH=/opt/hackathon.db

WORKDIR /opt/api

RUN pip install fastapi uvicorn sqlalchemy
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]