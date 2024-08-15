# Use  Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /my_api

# Copy the requirements # Using '.' to avoid path redundancy.
COPY requirements.txt .  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files container # Using '.' for already set.
COPY . .  

# port the container will run on
EXPOSE 8081

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8081", "my_api:app"]

