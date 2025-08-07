# 🚀 Cloud-Native Web Application Deployment on AWS EKS

This project demonstrates a complete CI/CD pipeline for deploying a Python-based web application using Docker, GitHub Actions, and AWS services such as EC2 and EKS (Elastic Kubernetes Service).

---

## 📌 Project Goals

- Automatically build and push Docker images to DockerHub on application changes.
- Deploy the updated Docker image to an EC2 instance using SSH.
- Extend the project to deploy the application on AWS EKS (Kubernetes).

---

## ⚙️ Workflows

### 1. CI/CD Docker Workflow

Triggered on every change to the application.

- Dockerizes the Python application.
- Pushes the image to DockerHub using GitHub Actions.

### 2. EC2 Deployment Workflow

Triggered after a successful Docker image push.

- SSH into an EC2 instance.
- Pulls the latest Docker image from DockerHub.
- Stops the running container (if any), and runs the new container with the latest changes.

> ✅ **Two-Week Goal**: Set up the workflows above and have a fully automated CI/CD pipeline in place.

---

## 🧠 Prerequisites

The user should have:

- 🧰 Basic knowledge of **Terraform**
- 🐳 Familiarity with **Docker**
- ☁️ Basic understanding of **AWS** (especially EC2 and EKS)
- 🔄 Experience with **CI/CD tools** (e.g., GitHub Actions)

---

## 🌐 Scope of the Project

- Provision infrastructure using Terraform.
- Set up CI/CD using GitHub Actions.
- Use Docker to containerize the app.
- Deploy the app first on EC2 via SSH, and later to **AWS EKS** for a more scalable, production-ready environment.

---

## 💡 What This Project Does

- Automates the containerization and deployment of a Python web application.
- Uses best practices in CI/CD and cloud-native development.
- Serves as a template for teams looking to deploy containerized apps on AWS EKS.

---

## 🤔 Why This Project is Useful

- Teaches real-world DevOps skills.
- Reduces manual deployment overhead.
- Provides a clear blueprint for modern cloud application delivery using Kubernetes.

---

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone the project**
   ```bash
   git clone https://github.com/abirthapa1/DevOpsPipeline.git
   cd DevOpsPipeline
   ```

## ec2-ssh using github actions

https://gist.github.com/raviagheda/c69ae5e884f4490b1af656dbd80c00dd

name: Deploy

on:
push:
branches: [ dev ]

jobs:
Deploy:
name: Deploy to EC2
runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Build & Deploy
        env:
            PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
            HOSTNAME: ${{secrets.SSH_HOST}}
            USER_NAME: ${{secrets.USER_NAME}}

        run: |
          echo "$PRIVATE_KEY" > private_key && chmod 600 private_key
          ssh -o StrictHostKeyChecking=no -i private_key ${USER_NAME}@${HOSTNAME} '

              # Now we have got the access of EC2 and we will start the deploy .
              cd /home/ubuntu/<PROJECT_DIRECTORY> &&
              git checkout dev &&
              git fetch --all &&
              git reset --hard origin/dev &&
              git pull origin dev &&
              sudo npm i &&
              sudo npm run build &&
              sudo pm2 stop ./dist/index.js &&
              sudo pm2 start ./dist/index.js
              '

#Test commit
