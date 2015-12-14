#!/bin/bash

POSTGRESQL_PASSWORD='AGPXSnTFHmXknK'
PROJECT_DIR=/var/www/chaos
cd $PROJECT_DIR

cp /default_settings.py /tmp/default_settings.py

sed "s/_ip_address_/$POSTGRESQL_PORT_5432_TCP_ADDR/" /tmp/default_settings.py > \
/tmp/default_settings.py_

# Replace password in application settings
sed "s/_password_/$POSTGRESQL_PASSWORD/" /tmp/default_settings.py_ > \
/default_settings.py

test -d venv || virtualenv venv
echo 'Activating virtual environment'
source venv/bin/activate

# Replace ip address in application settings
/bin/bash -c "echo 'CHAOS_CONFIG_FILE=/default_settings.py' >> /.env"

if [ ! -e ./venv/.installed_requirements ]
then
    pip install -r requirements.txt
    pip install -r /requirements-dev.txt

    touch ./venv/.installed_requirements
fi

./setup.py build_pbf

honcho run ./manage.py db upgrade

if [ ! -e ./venv/.inserted_queries ]
then
    SQL_QUERIES=$(cat <<'QUERIES'
    INSERT INTO category(created_at, id, name, is_visible, client_id)
    SELECT
    '2015-01-26 10:41:53.707955','f144f6a0-a547-11e4-9e0e-00249b0dbf3d', 'Trafic inopinée', True, c.id
    FROM client c LIMIT 1;

    INSERT INTO category(created_at, id, name, is_visible, client_id)
    SELECT '2015-01-26 10:41:53.707955','1144f6a0-a547-11e4-9e0e-00249b0dbf3d', 'Trafic prévue', True, c.id
    FROM client c LIMIT 1;

    INSERT INTO category(created_at, id, name, is_visible, client_id)
    SELECT '2015-01-26 10:41:53.707955','2144f6a0-a547-11e4-9e0e-00249b0dbf3d', 'Evénementielle', True, c.id
    FROM client c LIMIT 1;

    INSERT INTO category(created_at, id, name, is_visible, client_id)
    SELECT '2015-01-26 10:41:53.707955','3144f6a0-a547-11e4-9e0e-00249b0dbf3d', 'Commerciale', True, c.id
    FROM client c LIMIT 1;

    INSERT INTO category(created_at, id, name, is_visible, client_id)
    SELECT '2015-01-26 10:41:53.707955','4144f6a0-a547-11e4-9e0e-00249b0dbf3d', 'Institutionnelle', True, c.id
    FROM client c LIMIT 1;
QUERIES
)
    touch ./venv/.inserted_queries
fi

export PGPASSWORD=$POSTGRESQL_PASSWORD
echo $SQL_QUERIES | psql -U navitia -h $POSTGRESQL_PORT_5432_TCP_ADDR chaos

honcho -d $PROJECT_DIR -f /Procfile.txt start
