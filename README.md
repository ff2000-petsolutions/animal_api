# FastAPI Animal Detection with DNN Frontend in Docker

This project sets up a local **FastAPI** backend for animal detection and integrates it with a **DotNetNuke (DNN)** frontend. The FastAPI backend uses Google Vision API to analyze uploaded images and classify them into predefined animal categories. The frontend enables users to upload an image, preview it, and view the detected animal categories.

This version is set up to run in **Docker** containers for easy local deployment.

---

## 🛠️ Prerequisites

Before deploying this project locally with Docker, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop) (For creating and running containers)
- Python 3.9+ (For building the FastAPI backend Docker image)
- Node.js and npm (For building the DNN frontend)
- **Google Cloud Vision API credentials** (Download and set up as `superb-webbing-455211-d7-2e140293e808.json`)
- **DotNetNuke** (DNN) setup for the frontend integration

---

## 🚀 Getting Started

Follow these steps to set up the backend and frontend locally with Docker.

### 1. Backend: FastAPI Setup in Docker

#### a. Create the Dockerfile for FastAPI Backend

1. Create a file named `Dockerfile` inside the backend directory:

    ```dockerfile
    # Use the official Python image from Docker Hub
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the requirements file into the container
    COPY requirements.txt .

    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the app files into the container
    COPY . .

    # Set the environment variable for Google Cloud credentials
    ENV GOOGLE_APPLICATION_CREDENTIALS="/app/superb-webbing-455211-d7-2e140293e808.json"

    # Expose port for FastAPI server
    EXPOSE 8000

    # Command to run the FastAPI app using Uvicorn
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

#### b. Create the `requirements.txt` for FastAPI Dependencies

1. Create a `requirements.txt` file inside the backend directory:

    ```
    fastapi
    uvicorn
    google-cloud-vision
    ```

#### c. Build and Run the Docker Container for FastAPI

1. Build the Docker image:

    ```bash
    docker build -t fastapi-animal-detection .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 fastapi-animal-detection
    ```

The FastAPI backend will now be running inside the container at `http://localhost:8000`.

---

### 2. Frontend: DNN Integration

#### a. DNN Module Integration

Ensure your **DNN** project is set up with the appropriate **MVC** configuration, including the HTML and JavaScript for uploading and analyzing images.

Update the **JavaScript** code in your `.cshtml` file to use the local FastAPI backend URL:

```javascript
fetch('http://localhost:8000/analyze', {
    method: 'POST',
    body: formData
})
