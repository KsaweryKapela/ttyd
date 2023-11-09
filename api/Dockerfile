FROM huggingface/transformers-pytorch-gpu

# Copy api files
RUN mkdir -p /opt/api
COPY . /opt/api
COPY hackathon.db /opt/hackathon.db
COPY translator.sh /opt/translator.sh

# Set envs
ENV https_proxy=
ENV HTTPS_PROXY=
ENV SQLITE_PATH=/opt/hackathon.db
ENV TRANS_PATH=/opt/translator.sh

# Install bash
# RUN apk add --no-cache bash

WORKDIR /opt/api
# COPY model model

# RUN apt-get update && \
#     apt-get install -y git git-lfs && \
#     git lfs install
# RUN git lfs clone https://huggingface.co/mistralai/Mistral-7B-v0.1

RUN pip install fastapi uvicorn
RUN pip install bitsandbytes


# Run api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
