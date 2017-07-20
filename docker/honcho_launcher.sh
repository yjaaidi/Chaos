#!/bin/bash

set -e

echo -n "Waiting for postgres and rabbitmq containers to be reachables..."
until nc -z database 5432 &&  nc -z rabbitmq 5672
do
    echo -n "."
    sleep 0.5
done
echo

exec /var/www/Chaos/docker/run.sh