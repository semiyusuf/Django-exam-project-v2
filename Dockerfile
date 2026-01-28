# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Prevent Python from buffering stdout/stderr (good for Docker logs)
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "mysite1/manage.py", "runserver", "0.0.0.0:8000"]
