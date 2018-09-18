# Use an official Python runtime as a parent image
FROM python:3.5-slim

# Set the working directory to /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y gcc

# Install any needed packages specified in requirements.txt
ADD ./requirements.txt /app/requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Define environment variable
ENV NAME World

# Copy the current directory contents into the container at /app
ADD ./fixtures /app
ADD ./apps /app/apps
ADD ./manage.py /app

RUN python3 manage.py --debug migrate
RUN python3 manage.py --debug loaddata db_data-070918 fiber-initial

ADD . /app

RUN python3 manage.py --debug migrate
# Make port 80 available to the world outside this container
EXPOSE 80
# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver", "--debug", "0.0.0.0:80"]
