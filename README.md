# Wisecow DevOps Project

## Project Overview

This project demonstrates containerization and deployment of the Wisecow application using Docker, Kubernetes (Minikube), and GitHub Actions CI/CD pipeline.

## Technologies Used

* Docker
* Kubernetes
* Minikube
* GitHub Actions
* Git
* Ubuntu

## Project Structure

```text
wisecow/
│
├── Dockerfile
├── wisecow.sh
├── README.md
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
└── .github/
    └── workflows/
        └── docker-build.yml
```

## Docker Setup

### Build Docker Image

```bash
docker build -t wisecow-app .
```

### Run Docker Container

```bash
docker run -d -p 4499:4499 --name wisecow-container wisecow-app
```

### Access Application

```text
http://localhost:4499
```

---

## Kubernetes Deployment

### Apply Deployment

```bash
kubectl apply -f k8s/deployment.yaml
```

### Apply Service

```bash
kubectl apply -f k8s/service.yaml
```

### Verify Pods

```bash
kubectl get pods
```

### Access Application via Minikube

```bash
minikube service wisecow-service
```

---

## CI/CD Pipeline

GitHub Actions workflow automatically:

* Triggers on push to main branch
* Builds Docker image
* Verifies successful build process

Workflow file:

```text
.github/workflows/docker-build.yml
```

---

## Features Implemented

* Dockerized Wisecow application
* Kubernetes deployment using Minikube
* Service exposure using NodePort
* GitHub Actions CI pipeline
* Public GitHub repository

---

## Screenshots

### Running Docker Container

![Running Docker Container](screenshots/running-docker-container.png)

### Kubernetes Pods

![Kubernetes Pods](screenshots/pods-running.png)

### Application Browser Output

![Browser Output](screenshots/wisecow-browser-output.png)

### GitHub Actions Successful Workflow

![GitHub Actions](screenshots/github-actions-success.png)

### Minikube Service Exposure

![Minikube Service](screenshots/minikube-service.png)
