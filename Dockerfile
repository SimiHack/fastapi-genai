# Use the official Python slim image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Ensure Uvicorn and FastAPI are installed
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uvicorn fastapi

# Use CMD in the correct format
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
