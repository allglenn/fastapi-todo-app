
---

# FastAPI To-Do List Application

## Introduction

This project is a To-Do List application built with FastAPI, a high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. The application is designed to be run in a Docker container, using MongoDB as the database for storing to-do items. This README outlines the steps for setting up, running, and deploying the application.

## Features

- Create, read, update, and delete (CRUD) to-do items.
- Dockerized application for easy setup and deployment.
- Utilizes MongoDB for data persistence.

## Technology Stack

- **FastAPI**: For creating RESTful APIs with Python.
- **Python**: The programming language used.
- **Docker**: For containerizing the application and its environment.
- **MongoDB**: NoSQL database for storing to-do items.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose are installed on your machine.
- Basic knowledge of Docker, Python, and MongoDB.

## Setup and Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/yourusername/fastapi-todo-app.git
   cd fastapi-todo-app
   ```

2. **Build and Run the Docker Container**

   ```
   docker-compose up --build
   ```

   This command builds the Docker image and starts the application and MongoDB database.

## Usage

Once the application is running, you can access the API at `http://localhost:80`.

### API Endpoints

- `GET /todos/`: Retrieve all to-do items.
- `POST /todos/`: Create a new to-do item.
- `PUT /todos/{todo_id}`: Update an existing to-do item.
- `DELETE /todos/{todo_id}`: Delete a to-do item.

You can use tools like Postman or cURL to interact with the API.

## Deployment

To deploy this application, you will need a server with Docker and Docker Compose installed. Transfer the application files to your server, and run the following command in the application directory:

```
docker-compose up --build -d
```

This will start the application in detached mode.

## Contributing

Contributions to this project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

glenn  - @glenn_all 
Project Link: https://github.com/allglenn/fastapi-todo-app


---
