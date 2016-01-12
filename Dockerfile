############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

FROM python:2.7-wheezy

# Requirements have to be pulled and installed here, otherwise caching won't work
ADD ./requirements /requirements

RUN apt-get update
RUN apt-get install -y libtiff4-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
RUN pip install -r /requirements/local.txt

RUN groupadd -r flask && useradd -r -g flask flask
ADD . /app
RUN chown -R flask /app

WORKDIR /app

# Expose ports
#EXPOSE 80
EXPOSE 8888
EXPOSE 5000

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
#CMD python server.py
CMD python run.py
