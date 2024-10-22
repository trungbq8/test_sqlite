# Use the official Python image as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Command to run the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
