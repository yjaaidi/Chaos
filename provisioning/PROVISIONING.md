# Provisioning

Install docker by following instructions from [http://docs.docker.com/engine/installation/](http://docs.docker.com/engine/installation/)

## PostgreSQL

Build PostgreSQL image

```
(cd  provisioning/postgresql && sudo docker build -t postgresql .)
```

Run PostgresSQL container in background

```
export POSTGRES_PASSWORD="%~\`4cj,|@snhg!''f@ay~"
sudo docker run \
--name chaos_postgresql \
-v `pwd`/provisioning/postgresql/logs:/var/log/postgresql \
-v `pwd`/provisioning/postgresql/data:/var/lib/postgresql \
-e PGPASSWORD=$POSTGRES_PASSWORD \
-e POSTGRES_PASS=$POSTGRES_PASSWORD \
-d -p 5432:5432 postgresql
```

## Application

Initalize git submodules

```
source provisioning/app/initialize-submodules.sh
```

Build application image

```
(cd provisioning/app && sudo docker build -t chaos .)
```

```
sudo docker run \
--link chaos_postgresql:postgresql \
-v `pwd`:/var/www/chaos \
-d -p 5000:5000 chaos
```

## FAQ

**How to connect to PostgreSQL running container?**

Execute the following command

```
# Use '%~`4cj,|@snhg!'f@ay~' as password (without surrounding single quote)
psql --username postgres --password -h 127.0.0.1 chaos
```

```
# Use 'AGPXSnTFHmXknK' as password (without surrounding single quote)
psql --username navitia --password -h 127.0.0.1 chaos
```

**How to remove the PostgreSQL container**

Remove postgres container

```
sudo docker rm -f `sudo docker ps -a | grep postgres | awk '{print $1}'`
```

Remove logs and database files

```
/bin/bash -c 'sudo rm -rf provisioning/postgresql/{logs,data}'
```

**How to access PostgresSQL container logs?**

Execute `Docker logs` command with `follow` (`-f`) option

```
suo docker logs -f `sudo docker ps -a | grep postgres | awk '{print $1}'`
```
