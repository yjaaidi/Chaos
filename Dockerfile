FROM alpine:edge

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN echo http://dl-3.alpinelinux.org/alpine/edge/testing  >> /etc/apk/repositories

RUN apk --update --no-cache add \
        g++ \
        build-base \
        python-dev \
        py2-pip \
        zlib-dev \
        linux-headers \
        musl \
        musl-dev \
        git \
        postgresql-dev && \
    pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir uwsgi && \
    apk del \
        g++ \
        build-base \
        python-dev \
        zlib-dev \
        linux-headers \
        musl \
        musl-dev

EXPOSE 5000

WORKDIR /usr/src/app/

ENV CHAOS_CONFIG_FILE=default_settings.py
ENV PYTHONPATH=.
CMD ["uwsgi", "--mount", "/=chaos:app", "--http", "0.0.0.0:5000"]

