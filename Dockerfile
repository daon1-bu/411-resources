# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy code into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your app (replace with your actual script
CMD ["python", "hello.py"]
