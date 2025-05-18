FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libsndfile1 \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Rust for sudachipy (TTS dependency)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    . "$HOME/.cargo/env"

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
    && pip install TTS pandas torch

CMD [ "bash" ]