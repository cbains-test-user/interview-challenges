# Spring Boot Demo

A simple Spring Boot REST API for managing users.

## Endpoints

- `GET /api/users` — List all users
- `GET /api/users/{id}` — Get user by ID
- `POST /api/users` — Create a new user
- `GET /actuator/health` — Health check

## Build & Run

```bash
mvn clean package
java -jar target/demo-0.0.1-SNAPSHOT.jar
```

## Docker

```bash
docker build -t demo .
docker run -p 8080:8080 demo
```

## Deploy

```bash
kubectl apply -f k8s/
```
