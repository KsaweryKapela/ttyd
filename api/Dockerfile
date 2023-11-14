FROM huggingface/transformers-pytorch-gpu

WORKDIR /opt/api
COPY . /opt/api
COPY EngFinDB.db /opt/EngFinDB.db

# Set envs
ENV https_proxy=
ENV HTTPS_PROXY=
ENV SQLITE_PATH=/opt/EngFinDB.db

WORKDIR /opt/api
RUN pip install peft
RUN pip install fastapi uvicorn
RUN pip install bitsandbytes


# Run api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]