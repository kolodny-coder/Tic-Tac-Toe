FROM python:3-alpine3.6

WORKDIR /app

ADD . /app

CMD ["python", "app.py" ]
