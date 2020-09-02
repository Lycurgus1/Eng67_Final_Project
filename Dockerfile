FROM python:3.8 AS app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]

# second stage build

FROM python:3.8-slim

COPY --from=app /usr/src/app /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]