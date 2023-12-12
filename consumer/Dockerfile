# Use a base image with Python and other dependencies
FROM python:3.8

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

# Create and set the working directory
WORKDIR /app


# Copy the requirements file into the container at /app
COPY consumer/requirements_consumer.txt /app/


# Install dependencies
RUN pip install --no-cache-dir -r requirements_consumer.txt

# Copy the current directory contents into the container at /app
COPY consumer/ /app/

# Command to run on container start
CMD ["python", "consumer.py"]
