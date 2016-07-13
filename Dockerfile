FROM debian:7.8

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
        curl \
        python2.7 \
        python2.7-dev \
        python-pip \
        git \
        libpq-dev \
        wget \
        netcat && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
RUN pip install -q honcho

RUN wget -qP /tmp https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz
RUN tar -xf /tmp/protobuf-2.6.1.tar.gz -C /var/lib/
RUN cd /var/lib/protobuf-2.6.1 && \
    ./configure && \
    make && \
    make install && \
    ldconfig
RUN rm -rf /tmp/*

ADD docker/run.sh /run.sh
RUN chmod 755 /run.sh

# fix python encoding warning
ENV PYTHONIOENCODING utf-8

WORKDIR /var/www/Chaos

EXPOSE 80

CMD ["/run.sh"]
