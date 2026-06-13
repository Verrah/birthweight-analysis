# ── Base image ────────────────────────────────────────────────
# Python 3.11 slim keeps the image small while including
# everything needed to run scientific Python code
FROM python:3.11-slim

# ── Metadata ──────────────────────────────────────────────────
LABEL maintainer="Verrah"
LABEL project="NCHS Birthweight Analysis 1969-1971"
LABEL version="1.0"

# ── System dependencies ───────────────────────────────────────
# gcc and build-essential are needed to compile numpy/scipy
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ── Set working directory ─────────────────────────────────────
WORKDIR /app

# ── Copy and install Python dependencies ─────────────────────
# Copy requirements first so Docker can cache this layer
# and avoid reinstalling packages on every code change
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ── Copy project source code ──────────────────────────────────
COPY src/ ./src/
COPY notebooks/ ./notebooks/

# ── Create directories for data and outputs ───────────────────
# Data is mounted at runtime; never baked into the image
RUN mkdir -p data outputs

# ── Environment variables ─────────────────────────────────────
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ── Expose Jupyter port ───────────────────────────────────────
EXPOSE 8888

# ── Default command: run validation script ───────────────────
# Override with 'docker run ... jupyter notebook' for
# interactive analysis
CMD ["python", "src/validate.py"]