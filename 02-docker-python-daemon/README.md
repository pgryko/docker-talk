# Python Daemons

Lots of programs need to be run as continuous running processes (called daemons)

"A daemon process is a process which runs in background and has no controlling terminal. Since a daemon process usually has no controlling terminal so almost no user interaction is required. Daemon processes are used to provide services that can well be done in background without any user interaction."

## Simple flask server
In this example, we will show a python flask server

```python
from flask import Flask

server = Flask(__name__)


@server.route("/")


def hello():
    return "Simple flask server"


if __name__ == "__main__":
    server.run(host='127.0.0.1')
```

New docker file:

```dockerfile
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
```

```bash
$ docker build --tag flask-server:1.0 .
```

Running a container

```bash
$ docker run --rm flask-server:1.0
```

Exec into a running container:
Get the container name:
```bash
$ docker container ls
```
Get a shell session
```bash
docker exec -it container-id /bin/bash
```

## Docker compose

Docker compose is a way of tying together different running containers.
E.g. a webserver may need a python server, a database and persistent volume

Additionally the commands around the docker compose are easier to remember
the those for docker compose

Useful commands:

```bash
# Build all the containers referenced in a docker compose
$ docker compose up
# Curl the server api
$ curl localhost:5000
# Rebuild the docker containers
$ docker-compose build
# Run the docker compose as daemon
$ docker-compose up -d
# Check status of docker containers
$ docker-compose ps
# View container logs
$ docker-compose logs
# Watch the container logs
$ docker-compose logs -f
# Shut down the docker container process and remove any associated volumes
$ docker-compose down -v
```