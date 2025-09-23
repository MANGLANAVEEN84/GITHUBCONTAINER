# Use the official Python base image with the latest version
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy your application code (if any)

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app

# Install any additional dependencies here

# Install Node.js 18 and npm (use default npm bundled with Node.js 18)
RUN apt-get update \
	&& apt-get install -y curl \
	&& curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
	&& apt-get install -y nodejs \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Install common frontend dependencies globally (optional, adjust as needed)
RUN npm install -g yarn vite create-react-app @angular/cli @vue/cli

# Update requirements.txt with installed packages each time the container starts
CMD pip freeze > /app/requirements.txt && python3
