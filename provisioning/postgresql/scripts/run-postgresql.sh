#!/bin/bash

# Enable job control (use of `%1` to resume a job in foreground)
set -m

postgres_dir='/var/lib/postgresql'
database_dir=$postgres_dir'/9.3/main'
test -d $database_dir || mkdir -p $database_dir

# restore copy of original PostgreSQL database
test -e $postgres_dir/PG_VERSION || cp -R /var/lib/_postgresql/* $postgres_dir

chown -R postgres $postgres_dir
chmod -R 0700 $postgres_dir

source /run.sh &

sleep 5
sudo -u postgres /scripts/create-postgresql-user-databases.sh

%1