# Provisioning

Install Docker by following instructions from [http://docs.docker.com/engine/installation/](http://docs.docker.com/engine/installation/)

Install Docker Compose by following instructions from [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

Initialize git submodules

```
source provisioning/app/initialize-submodules.sh
```

Build the required images

```
(cd provisioning && sudo docker-compose build)
```

Run PostgreSQL and application containers

```
(cd provisioning && sudo docker-compose  --x-networking up)
```

## FAQ

**How to build a PostgreSQL image for Chaos?**

Execute the following command to change the current directory and build PostgreSQL image

```
(cd  provisioning/postgresql && sudo docker build -t postgresql .)
```

**How to run PostgresSQL container manually in background?**

Execute the following commands in order to
 * export respectively development `postgres` and `navitia` passwords
 * run a database container

```
export POSTGRES_PASSWORD="%~\`4cj,|@snhg!''f@ay~"
export NAVITIA_PASSWORD=AGPXSnTFHmXknK
sudo docker network create provisioning
sudo docker run \
--net=provisioning \
--name chaos_database \
-v `pwd`/provisioning/postgresql/logs:/var/log/postgresql \
-v `pwd`/provisioning/postgresql/data:/var/lib/postgresql \
-e PGPASSWORD=$POSTGRES_PASSWORD \
-e NAVITIA_PASSWORD=$NAVITIA_PASSWORD \
-e POSTGRES_PASS=$POSTGRES_PASSWORD \
-d postgresql
```

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
sudo docker logs -f `sudo docker ps -a | grep postgres | awk '{print $1}'`
```

**How to build Chaos application image?**

```
(cd provisioning/app && sudo docker build -t chaos .)
```

**How to run Chaos application image?**

After having executed the command to run manually the PostgreSQL container,
run the next commands in order to
 * export development `navitia` password
 * run an application container

```
export NAVITIA_PASSWORD=AGPXSnTFHmXknK
sudo docker run \
--net=provisioning \
-e PGPASSWORD=$NAVITIA_PASSWORD \
-v `pwd`:/var/www/chaos \
-d -p 5000:5000 chaos
```

