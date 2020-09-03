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

## Creating A Docker EC2 instance

- Within AWS we will create an EC2 instance 

![](/images/create-docker-app.png)


  
- We will then provision it with Docker using the follwoing commands

```

```

- The following command will delete all images
```commandline
sudo docker rmi -f $(docker images -a -q)
```

# Running our Flask Application

- If the person running the application has the access and secret keys stored as an environment variable, all they would have to do
is run the bellow command

```commandline
sudo docker run -e AWS_ACCESS_KEY=$AWS_ACCESS_KEY -e AWS_SECRET_KEY=$AWS_SECRET_KEY -d -t -p 5000:5000 bariallali/flask_final_app:20
```