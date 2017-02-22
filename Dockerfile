FROM debian:jessie

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
        wget \
        python-pip \
        libpq5 \
        libprotobuf9 \
        libpython2.7 \
        netcat \
        && \
    rm -rf /var/lib/apt/lists/*

COPY . /srv/chaos
WORKDIR /srv/chaos

RUN set -xe && \
    buildDeps="libpq-dev python-dev protobuf-compiler git" && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install $buildDeps && \
    pip install uwsgi && \
    pip install -r requirements.txt && \
    python setup.py build_pbf && cd .. && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 5000

ENV CHAOS_CONFIG_FILE=default_settings.py
ENV PYTHONPATH=.
CMD ["uwsgi", "--mount", "/=chaos:app", "--http", "0.0.0.0:5000"]
