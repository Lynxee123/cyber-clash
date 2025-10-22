# Use a lightweight base Python image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Install necessary system dependencies for Pygame
# This is crucial for graphical output
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0

# Copy project files into the container
# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Run the command to run pygame application
CMD ["python", "main.py"]