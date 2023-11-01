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

# Install requirements
RUN apt-get update && apt-get install -y curl gnupg2

RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && apt-get update
RUN apt-get install -y nvidia-container-toolkit
RUN pip install fastapi uvicorn
WORKDIR /opt/api

# Run api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
