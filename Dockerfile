FROM ubuntu:18.04

WORKDIR /app

ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y python3 \
    python3-psycopg2 \
    libpq-dev \
    python3-pip \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    python3-dev

RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN scripts/build_model.sh