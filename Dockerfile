# Use an official Python runtime as a parent image
FROM pytorch/pytorch:latest

# Set the working directory to /workspace
WORKDIR /workspace

# Copy the current directory contents into the container at /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install python-pip -y && \
    pip install pandas matplotlib
  



