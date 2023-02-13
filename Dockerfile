FROM python:3.11.2-alpine3.17

RUN mkdir /data

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]