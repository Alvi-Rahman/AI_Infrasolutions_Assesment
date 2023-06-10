# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables for Python buffering and encoding
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . .

# Expose the port on which the Django app will run (modify if needed)
EXPOSE 8000

# Run Django development server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
