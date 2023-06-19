# Use the official Python image as the base image
FROM python:3.11-bullseye

RUN pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY requirements.txt /app/

# Install poetry
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Expose the port your Flask application will run on
EXPOSE 8000

# Run the Flask application
CMD ["python", "vicunapi.py"]%   