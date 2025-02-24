# Use ARM64-compatible base image explicitly
FROM --platform=linux/arm64 python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Ensure correct installation of uvicorn & fastapi
RUN pip install --no-cache-dir --force-reinstall uvicorn fastapi

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
