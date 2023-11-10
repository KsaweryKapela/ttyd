FROM huggingface/transformers-pytorch-gpu

# Copy api files
RUN mkdir -p /opt/api
COPY . /opt/api
COPY hackathon.db /opt/hackathon.db

ENV SQLITE_PATH=/opt/hackathon.db

WORKDIR /opt/api
# COPY model model

# RUN apt-get update && \
#     apt-get install -y git git-lfs && \
#     git lfs install
# RUN git lfs clone https://huggingface.co/mistralai/Mistral-7B-v0.1

RUN pip install fastapi uvicorn sqlalchemy
RUN pip install bitsandbytes
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]