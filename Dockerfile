FROM navitia/python

WORKDIR /usr/src/app
COPY . /usr/src/app

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
    pip install --no-cache-dir -r requirements.txt && \
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

