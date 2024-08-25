# 🚀 Project Description

This project is a microservices-based application that is made up of several independent services, each of which handles a specific part of the application's functionality. The main goal of the project was to containerize each of these microservices using Docker and then run them together using Docker Compose.

## 🛠️ Technologies Used

- 🐳 **Docker**: To containerize each of the microservices.
-    **Docker Compose**: To orchestrate and manage the execution of the different microservices.
- ⚙️ **Golang**: For the development of the Auth API.
- 🌐 **Node.js**: For the development of the Frontend and the TODOs API.
- 🐍 **Python**: For the development of the Log Message Processor.
- ☕ **Java (Spring Boot)**: For the development of the Users API.
- 📦 **Redis**: Used as middleware for communication between some services.

## 📋 Containerization and Execution Process

1. **🔄 Repository Cloning**

   The first thing I did was clone the `microservice-app-example` repository from GitHub, which contained the source code for all the microservices.

   ```bash
   git clone https://github.com/bortizf/microservice-app-example.git

## 📦 Creation of Dockerfiles for Each Microservice

2. Each microservice had its own Dockerfile, where I defined how to build the Docker image for each of them:

- **Auth API**: This service was developed in Golang, so I used a base Golang image to compile the binary and then a minimalist (distroless) image to run it.
- **Users API**: Developed in Java using Spring Boot. An openjdk image was used to build and run the application.
- **Log Message Processor**: This service, written in Python, uses Redis to process messages. I used a base Python image to install the dependencies and run the application.
- **ALL APIs and Frontend**: Both services were developed in Node.js, so I used a Node.js image to install the dependencies and run the applications.

## 🔨 Construction and Execution of Containers

3. Used Docker Compose to manage the build and execution of all microservices. The `docker-compose.yml` file that defines these services is located in the root folder of the project.

## 🚀 Project Execution

4. To run all the microservices, I simply used the following command:

  ```bash
  docker-compose up --build
```

  This command builds Docker images for each service, starts them, and connects them to the same Docker network (`app-network`), allowing them to communicate with each other.

## 🌐 Summary of Services and Ports

- **Auth API**: Running on [http://localhost:8000](http://localhost:8000)
- **Users API**: Running on [http://localhost:8083](http://localhost:8083)
- **ALL APIs**: Running on [http://localhost:8082](http://localhost:8082)
- **Frontend**: Running on [http://localhost:8080](http://localhost:8080)
- **Redis**: Listening on port `6379`

Each of these services exposes a port on the host system so they are accessible from the outside, while Docker Compose connects them into a common internal network so they can communicate with each other.

## 📚 Conclusion

The project consisted of containerizing and deploying an application made up of several microservices. Using Docker and Docker Compose, I was able to run and orchestrate these services efficiently, ensuring that all components worked together as a cohesive system. Configuring networks and ports was key to allowing internal communication between services and exposing user interfaces and APIs to the outside.

##Architecture

Take a look at the components diagram that describes them and their interactions.
![microservice-app-example](/arch-img/Microservices.png)
