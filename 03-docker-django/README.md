# Django **DEVELOPMENT** server

A more complex example of using docker compose with multiple docker containers
running daemon process. This is the kind of thing you will see in a dev
environment.

Note, this runs a development server without key security features.
Do NOT use this in production. What's missing is:

- A secure secret key is not set
- SSL/TLS encryption
- Secure Database authentication
- Backups
- Site hardening (allowed hosts/debug settings etc)
- Static asset serving and using a proper WSGI
- Monitoring

usually you'll have something similar to this docker compose for development,
and a hardened version, or other deployment solution (using the base docker images)
for production.

## Docker files

```dockerfile
FROM python:3.9-slim

# Update base packages and install updates
# Note these will be cached
RUN set -eux; \
	apt-get update; \
	apt-get upgrade -y; \
	apt-get install -y --no-install-recommends \
		wait-for-it; \
	rm -rf /var/lib/apt/lists/* ; \
	python -m pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY examplesite/requirements.txt /app

RUN pip install -r requirements.txt

# Copy the src directory contents into the container at /app
COPY examplesite/ /app

# CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
CMD ["wait-for-it", "$DB_HOST:5432", "--", "python",  "manage.py", "runserver"]
```

```dockerfile
FROM postgres:13

COPY files/init-db.sh /docker-entrypoint-initdb.d/init-db.sh

ENV POSTGRES_USER="postgres"
ENV POSTGRES_HOST_AUTH_METHOD="trust"
```

Create a sample django application

```bash
$ django-admin startproject examplesite
```

Use python decouple and configure settings file