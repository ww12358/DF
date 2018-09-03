#FROM ubuntu:16.04
FROM rcsa/python2-hdf5

RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app
COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/
RUN  chgrp -R www-data /usr/src/app/creek
RUN  chmod -R g+r /usr/src/app/creek

#CMD [ "gunicorn --pythonpath=/usr/src/app/creek/ app:app -w 2 -b 127.0.0.1:8000" ]