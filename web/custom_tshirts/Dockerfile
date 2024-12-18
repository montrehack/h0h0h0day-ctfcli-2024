# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r App/requirements.txt
RUN echo "flag{SSTI_vulnerability_is_very_dangerous}" > /app/flag.txt
# Make port 15685 available to the world outside this container
EXPOSE 15685

# Define environment variables
ENV FLASK_APP=App/server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run","--port","15685"]