FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY meta_llama_3.1_8B_abliterated.py .
#COPY ./meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf /app/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf

CMD ["python", "-u", "meta_llama_3.1_8B_abliterated.py"]