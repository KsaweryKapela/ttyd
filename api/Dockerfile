FROM python:3.7-alpine

# Copy api files
RUN mkdir -p /opt/api
COPY . /opt/api

# Set envs
ENV https_proxy=
ENV HTTPS_PROXY=
ENV SQLITE_PATH=/opt/hackathon.db

# Install bash
RUN apk add --no-cache bash

# Install requirements
RUN pip install fastapi uvicorn

EXPOSE 80

WORKDIR /opt/api

# Run api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
