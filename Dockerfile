FROM python:3-slim

WORKDIR /home/clowder
COPY templates /home/clowder/templates

COPY generator.py requirements.txt /home/clowder/
RUN pip3 install -r requirements.txt

CMD python3 generator.py
