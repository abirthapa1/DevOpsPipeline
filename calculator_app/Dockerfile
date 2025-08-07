# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

# Setting up the working dir
WORKDIR /calculator_app

# Copying the required files
COPY . .

# Installing the required packages into the container
RUN pip3 install -r requirements.txt

# Exposing the container to port 5000
EXPOSE 5000

# running the application as a module
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]