    # Use a Python base image
    FROM python:3.9-slim

    # Set the working directory
    WORKDIR /app

    # Copy the requirements file
    COPY requirements.txt .

    # Install the Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    RUN pip install --upgrade pymongo

    # Copy the application code
    COPY . .

    # Expose the required port
    EXPOSE 8000

    # Start the web server
    CMD ["python", "app.py"]
