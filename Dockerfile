# Use official Python runtime
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
COPY notebooks/rfm_segmentation_pipeline.pkl ./notebooks/

RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Run the app with gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "--timeout", "120", "app:app"]


