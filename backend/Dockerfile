FROM python:3.9
RUN python3.9 -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get upgrade -y
# RUN apt-get install -y default-mysql-client ffmpeg libsm6 libxext6

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .