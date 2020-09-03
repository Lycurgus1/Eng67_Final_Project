FROM python:3.8 AS app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt


# second stage build

FROM python:3.8-slim

COPY --from=app /usr/src/app /usr/src/app

WORKDIR /usr/src/app

ENV AWS_ACCESS_KEY=$AWS_ACCESS_KEY

ENV AWS_SECRET_KEY=$AWS_SECRET_KEY

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]


