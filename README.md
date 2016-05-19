# Chaos
Chaos is the web service which implements the real-time aspect of Navitia

## Installation

### Clone the repository Chaos
```
git clone git@github.com:CanalTP/Chaos.git
cd Chaos
```

### Python requirements
- Install Python `sudo apt-get install python2.7 python2.7-dev`
- Install [pip](https://pip.pypa.io/en/latest/installing/)
- Install [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html)

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Build protobufs
Install [protobuf v2.6.1](https://github.com/google/protobuf/blob/master/src/README.md)
```
git submodule init
git submodule update
./setup.py build_pbf
```

### Create the database
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

## Run Chaos with honcho (optional)
### Install honcho
You can use [honcho](https://github.com/nickstenning/honcho) for managing Procfile-based applications.

```
pip install honcho
```

### create a `.env` file
Write this line inside
```
CHAOS_CONFIG_FILE=default_settings.py
```

### Upgrade database

```
honcho run ./manage.py db upgrade
```

### RabbitMQ (optional)
RabbitMQ is optional and you can deactivate it if you don't want to send disruptions to a queue.

```
# chaos/default_settings.py
ENABLE_RABBITMQ = False
```

### Run Chaos
```
honcho start
```

## Tests
Create an .env file in tests/ with:
```
CHAOS_CONFIG_FILE=../tests/testing_settings.py
PYTHONPATH=..
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

## Provisioning

Provisioning instructions can be followed from [provisioning/PROVISIONING.md](provisioning/PROVISIONING.md)