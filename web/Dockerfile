#FROM ubuntu:16.04
FROM rcsa/python2-hdf5
RUN apt-get update && apt-get install -y cron && apt-get install -y tzdata &&\
    rm -r /var/lib/apt/lists/*

#set time zone for cron jobs
ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN pip install --upgrade pip

RUN mkdir -p /usr/src/app/creek/data/log/
COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app/
RUN  chgrp -R www-data /usr/src/app/creek
RUN  chmod -R g+r /usr/src/app/creek


# Add crontab file in the cron directory
ADD crontab /etc/cron.d/dy-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/dy-cron

# Create the log file to be able to run tail
RUN touch /usr/src/app/creek/data/log/dy.log
# Run the command on container startup

#CMD ["update-rc.d cron defaults && /etc/init.d/cron start"]
#CMD /usr/sbin/cron && tail -f /usr/src/app/creek/data/log/dy.log