FROM 097788601444.dkr.ecr.eu-west-1.amazonaws.com/proxy/library/python:3.11.2-alpine3.17

RUN mkdir /data

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]