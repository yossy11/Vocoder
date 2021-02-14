FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update && apt-get install -y libsndfile1
RUN pip install autopep8 flake8
RUN pip install -r requirements.txt
