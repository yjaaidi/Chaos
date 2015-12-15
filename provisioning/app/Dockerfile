FROM ubuntu:15.10

MAINTAINER Kisio Digital

# Update source repositories and install packages using aptitude

RUN apt-get update -y

RUN apt-get install -y wget python python-dev python-pip \
libpq-dev rabbitmq-server git postgresql-client

RUN pip install virtualenv

WORKDIR /tmp

RUN wget https://protobuf.googlecode.com/svn/rc/protobuf-2.6.0.tar.gz

# Build protobuf

RUN tar zxvf protobuf-2.6.0.tar.gz

RUN cd protobuf-2.6.0 && ./configure && make && make check && make install

RUN ldconfig

RUN rm -rf /tmp/protobuf-2.6.0

RUN mkdir -p /var/www/chaos

ADD default_settings.py /default_settings.py

ADD requirements-dev.txt /requirements-dev.txt

ADD run-server.sh /usr/local/bin/run-server.sh

ADD Procfile.txt /Procfile.txt

RUN chmod 0700 /usr/local/bin/run-server.sh

# Fix "Your terminal is not configured to receive UTF-8 encoded text" warning
ENV PYTHONIOENCODING utf-8

ENV CHAOS_CONFIG_FILE "/default_settings.py"

WORKDIR /var/www/chaos

VOLUME /var/www/chaos

EXPOSE 5000

CMD ["/usr/local/bin/run-server.sh"]
