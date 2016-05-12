# Chaos

Chaos is the web service which implements the real-time aspect of Navitia

## Installation

Installation instructions can be followed from [http://confluence.canaltp.fr/display/SPEED/Installation+et+utilisation+de+Chaos+en+local](http://confluence.canaltp.fr/display/SPEED/Installation+et+utilisation+de+Chaos+en+local)

### Python & Protobuf

1) Install [`pip`](https://pip.pypa.io/en/latest/installing/) and [`virtualenv`](http://virtualenv.readthedocs.org/en/latest/installation.html)

2) Install Python dependencies

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You need to compile `protobuf` files before using chaos:

```
# Add `protobuf` files to the `proto` directory
# before executing the following command
./setup.py build_pbf
```

## Provisioning

Provisioning instructions can be followed from [provisioning/PROVISIONING.md](provisioning/PROVISIONING.md)

## Optional: Honcho

You can run all the tests using honcho so you can install it this way:

```
pip install honcho
```

## Export CHAOS_CONFIG_FILE

In order to allow database upgrade with honcho, you have to set the path to the default configuration file in an env var.
For example:

```
export CHAOS_CONFIG_FILE=./default_settings.py
```

Or you can create a `.env` file with this line:

```
CHAOS_CONFIG_FILE=default_settings.py
```

## Update database

```
source venv/bin/activate
honcho run ./manage.py db upgrade
```

## Change schema database

```
source venv/bin/activate
honcho run ./manage.py db migrate
```
