# Use the official Python image as the base image
FROM python:3.11-bullseye

ADD https://huggingface.co/vicuna/ggml-vicuna-13b-1.1/resolve/main/ggml-vic13b-q5_1.bin /var/tmp/
RUN chmod +x /var/tmp/ggml-vic13b-q5_1.bin 

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