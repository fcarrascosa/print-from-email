FROM python:3-alpine

COPY ./src /script
COPY ./config /config

WORKDIR /script

RUN pip install -r requirements.txt

CMD python main.py