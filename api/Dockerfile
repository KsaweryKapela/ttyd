FROM huggingface/transformers-pytorch-gpu

WORKDIR /opt/api
COPY . /opt/api

# COPY model model
# RUN apt-get update && \
#     apt-get install -y git git-lfs && \
#     git lfs install
# RUN git lfs clone https://huggingface.co/mistralai/Mistral-7B-v0.1

RUN pip install fastapi uvicorn sqlalchemy
RUN pip install bitsandbytes peft
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]