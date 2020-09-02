# Containerisation and Deployment of our Final Project


## Creating A Docker File

#### - Crating a Dockerfile will allow our Jenkins pipeline to create an image of our application

![](/images/build-docker-image.png)

#### - We first create a basic DockerFile that will create a Python image with our application

```
FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]

```

#### - After this, we have created a multi-stage build which redcues the size of the application by 80% using the following code

```
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

CMD [ "python", "main.py" ]

```




- Running the below application will allow us to see our app run in interactive mode
```
sudo docker run -d -t bariallali/python_final_app:12
```