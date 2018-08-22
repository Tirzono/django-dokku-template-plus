FROM python:3.6-stretch

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# We expect our code to be mounted as a volume.
VOLUME /app

# Start all commands in the toolkit project directory.
WORKDIR /app/{{ project_name }}

