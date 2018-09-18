# Use an official Python runtime as a parent image
FROM python:3.5-slim
# Set the working directory to /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y gcc
RUN apt-get install -y mysql-client

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY ./requirements/prod.txt /app/requirements/prod.txt
RUN pip install --trusted-host pypi.python.org -r requirements/prod.txt

# Copy the current directory contents into the container at /app
RUN mkdir -p /etc/secrets && \
	echo phillippasswd > /etc/secrets/db_pass.secret && \
	echo phillipsecret > /etc/secrets/secret_key.secret
COPY ./apps /app/apps
COPY ./manage.py /app/manage.py
RUN python3 manage.py migrate
COPY ./fixtures /app/fixtures
RUN python3 manage.py loaddata db_data-070918 fiber-initial
COPY ./templates /app/templates
# Make port 80 available to the world outside this container
EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
