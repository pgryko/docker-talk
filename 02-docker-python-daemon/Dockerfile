FROM python:3.9-slim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY main.py /app

# CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
CMD ["python",  "main.py"]
