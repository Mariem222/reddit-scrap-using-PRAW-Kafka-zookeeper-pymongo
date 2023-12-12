# Use the official Python image as the base image
FROM python:3.8-slim

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python development headers
RUN apt-get update && apt-get install -y \
    python3.8-dev \
    && rm -rf /var/lib/apt/lists/*

# Install librdkafka and its development headers
RUN apt-get update && apt-get install -y \
    librdkafka-dev \
    && rm -rf /var/lib/apt/lists/*


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY producer/requirements_producer.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements_producer.txt

# Copy the current directory contents into the container at /app
COPY producer/ /app/

# Command to run on container start
CMD ["python", "producer.py"]
