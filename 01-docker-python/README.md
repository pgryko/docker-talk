# Containerising a simple python program

## A simple python script to print out n'th Fibonacci numbers:

Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is:

```math
F_0=0,\quad F_1= 1
```
```math
F_n=F_{n-1} + F_{n-2}
```
for
```math
n>1
```

Often used as a simple example of recursion

``` python
import argparse


def fibonacci(n: int):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print the first N terms of the Fibonacci sequence')
    parser.add_argument('integer', type=int, nargs='?',
                        help='Number of elements to print')
    args = parser.parse_args()
    print(fibonacci(args.integer))
```

## A simple docker file
Each line in a docker file is an image layer

```dockerfile
# Load a specific image
FROM python:3.9-slim
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py /app

# ENTRYPOINT is to set the image’s main command,
# allowing that image to be run as though it was that command (and then use CMD as the default flags).
ENTRYPOINT ["python",  "main.py"]
# CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
#CMD [""]
```

## Building and running

Docker file needs to be built. We add a tag
for easy description

```bash
$ docker build --tag docker-python:1.0 .
```

Multiple rebuilds cache layers.
Running a container

```bash
$ docker run --rm docker-python:1.0
```

### Useful commands

Run a command in a new container:
```bash
$ docker run [IMAGE] [COMMAND]
$ docker run --rm [IMAGE] – removes a container after it exits.

$ docker run -td [IMAGE] – starts a container and keeps it running.

$ docker run -it [IMAGE] – starts a container, allocates a pseudo-TTY connected to the container’s stdin, and creates an interactive bash shell in the container.

$ docker run -it --rm [IMAGE] – creates, starts, and runs a command inside the container. Once it executes the command, the container is removed.

Delete a container (if it is not running):

$ docker rm [CONTAINER]
Update the configuration of one or more containers:

$ docker update [CONTAINER]
```
## Image 

List all images

```bash
$ docker image ls
```

Remove docker image

```bash
$ docker image rm docker-python:1.0
```

## Running a shell inside a docker container

Comment out the ENTRYPOINT and make sure the CMD is set.
The CMD is overwriteable
```dockerfile
#ENTRYPOINT ["python",  "main.py"]
# CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
# E.g. append a default value of 10
CMD ["python",  "main.py", "5"]
```

```bash
$ docker run -it --rm docker-python:1.0 /bin/bash
```