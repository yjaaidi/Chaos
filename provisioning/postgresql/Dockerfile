FROM tutum/postgresql

MAINTAINER Kisio Digital

ADD scripts /scripts

RUN chmod -R 755 /scripts

RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.utf8

# make backup of original database
RUN cp -R /var/lib/postgresql /var/lib/_postgresql

WORKDIR /

EXPOSE 5432

CMD ["/scripts/run-postgresql.sh"]
