FROM python:3.9-slim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py /app

# ENTRYPOINT is to set the image’s main command,
# allowing that image to be run as though it was that command (and then use CMD as the default flags).
ENTRYPOINT ["python",  "main.py"]
# CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
# E.g. append a default value of 10
#CMD ["5"]