# 🚀 Descripción del Proyecto

Este proyecto es una aplicación basada en microservicios que se compone de varios servicios independientes, cada uno de los cuales maneja una parte específica de la funcionalidad de la aplicación. El objetivo principal del proyecto era contenerizar cada uno de estos microservicios utilizando Docker y luego ejecutarlos de manera conjunta mediante Docker Compose.

## 🛠️ Tecnologías Utilizadas

- 🐳 **Docker**: Para contenerizar cada uno de los microservicios.
- 🧩 **Docker Compose**: Para orquestar y gestionar la ejecución de los diferentes microservicios.
- ⚙️ **Golang**: Para el desarrollo del Auth API.
- 🌐 **Node.js**: Para el desarrollo del Frontend y el TODOs API.
- 🐍 **Python**: Para el desarrollo del Log Message Processor.
- ☕ **Java (Spring Boot)**: Para el desarrollo del Users API.
- 📦 **Redis**: Utilizado como middleware para la comunicación entre algunos servicios.

## 📋 Proceso de Contenerización y Ejecución

1. **🔄 Clonación del Repositorio**

   Lo primero que hice fue clonar el repositorio `microservice-app-example` desde GitHub, el cual contenía el código fuente de todos los microservicios.

   ```bash
   git clone https://github.com/bortizf/microservice-app-example.git

## 📦 Creación de Dockerfiles para Cada Microservicio

2. Cada microservicio tenía su propio Dockerfile, donde definí cómo construir la imagen Docker para cada uno de ellos:

- **Auth API**: Este servicio fue desarrollado en Golang, por lo que usé una imagen base de Golang para compilar el binario y luego una imagen minimalista (distroless) para ejecutarlo.
- **Users API**: Desarrollado en Java usando Spring Boot. Se usó una imagen de openjdk para construir y ejecutar la aplicación.
- **Log Message Processor**: Este servicio, escrito en Python, utiliza Redis para procesar mensajes. Usé una imagen base de Python para instalar las dependencias y ejecutar la aplicación.
- **TODOs API y Frontend**: Ambos servicios fueron desarrollados en Node.js, por lo que usé una imagen de Node.js para instalar las dependencias y ejecutar las aplicaciones.

## 🔨 Construcción y Ejecución de los Contenedores

3. Utilicé Docker Compose para gestionar la construcción y ejecución de todos los microservicios. El archivo `docker-compose.yml` que define estos servicios se encuentra en la carpeta raíz del proyecto.

## 🚀 Ejecución del Proyecto

4. Para ejecutar todos los microservicios, simplemente utilicé el siguiente comando:

  ```bash
  docker-compose up --build
  Este comando construye las imágenes de Docker para cada servicio, las inicia y las conecta en la misma red de Docker (`app-network`), permitiendo que se comuniquen entre sí.

## 🌐 Resumen de los Servicios y Puertos

- **Auth API**: Ejecutándose en [http://localhost:8000](http://localhost:8000)
- **Users API**: Ejecutándose en [http://localhost:8083](http://localhost:8083)
- **TODOs API**: Ejecutándose en [http://localhost:8082](http://localhost:8082)
- **Frontend**: Ejecutándose en [http://localhost:8080](http://localhost:8080)
- **Redis**: Escuchando en el puerto `6379`

Cada uno de estos servicios expone un puerto en el sistema host para que sean accesibles desde el exterior, mientras que Docker Compose los conecta en una red interna común para que puedan comunicarse entre sí.

## 📚 Conclusión

El proyecto consistió en contenerizar y desplegar una aplicación compuesta por varios microservicios. Mediante Docker y Docker Compose, logré ejecutar y orquestar estos servicios de manera eficiente, garantizando que todos los componentes funcionaran juntos como un sistema cohesivo. La configuración de redes y puertos fue clave para permitir la comunicación interna entre los servicios y la exposición de las interfaces de usuario y API al exterior.

## Architecture

Take a look at the components diagram that describes them and their interactions.
![microservice-app-example](/arch-img/Microservices.png)
