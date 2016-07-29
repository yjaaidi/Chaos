# Chaos
Chaos is the web service which can feed [Navitia](https://github.com/CanalTP/navitia) with real-time [disruptions](http://doc.navitia.io/#traffic-reports).
It can work together with [Kirin](https://github.com/CanalTP/kirin) which can feed [Navitia](https://github.com/CanalTP/navitia) with real-time delays.

## Installation

### The hard way

#### Clone the Chaos repository
```
git clone git@github.com:CanalTP/Chaos.git
cd Chaos
```

#### Python requirements
- Install Python `sudo apt-get install python2.7 python2.7-dev`
- Install [pip](https://pip.pypa.io/en/latest/installing/)
- Install [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html)

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Build protobufs
Install [protobuf v2.6.1](https://github.com/google/protobuf/blob/master/src/README.md)
```
git submodule init
git submodule update
./setup.py build_pbf
```

#### Create the database
```
sudo apt-get install postgresql libpq-dev
sudo -i -u postgres
# Create a user
createuser -P navitia (password "navitia")

# Create database
createdb -O navitia chaos

# Create database for tests
createdb -O navitia chaos_testing
ctrl + d
```

#### Run Chaos with honcho (optional)
##### Install honcho
You can use [honcho](https://github.com/nickstenning/honcho) for managing Procfile-based applications.

```
pip install honcho
```

##### create a `.env` file
Write this line inside
```
CHAOS_CONFIG_FILE=default_settings.py
```

##### Upgrade database

```
honcho run ./manage.py db upgrade
```

##### RabbitMQ (optional)
RabbitMQ is optional and you can deactivate it if you don't want to send disruptions to a queue.

```
# chaos/default_settings.py
ENABLE_RABBITMQ = False
```

##### Run Chaos
```
honcho start
```

#### The easy way (with Docker)

```
git clone git@github.com:CanalTP/Chaos.git
cd Chaos
git submodule init
git submodule update
docker-compose up -d
```

To watch logs output: 
```
docker-compose logs -f
``` 

Chaos will be accessible on http://chaos_ws_1.docker if you are using the [docker-gen-hosts tool](https://github.com/vincentlepot/docker-gen-hosts), it will also be accessible on http://chaos-ws.local.canaltp.fr 

## Tests

The following commands for tests are also working in Docker environment, you just have to run before: 
```
docker-compose exec ws bash
cd tests
```

### Unit tests
```
honcho run nosetests
```

### Functional tests
```
cd tests
honcho run lettuce
```
To stop directly on faulty test
```
honcho run lettuce --failfast
```


