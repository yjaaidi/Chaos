#!/bin/bash

# Wait for the database to be online
# See also https://github.com/docker/compose/issues/374
sleep 10

DATABASE_HOST='chaos_database'
PROJECT_DIR=/var/www/chaos

cd $PROJECT_DIR

echo 'PostgreSQL database will listen on port port 5432 of host "'$DATABASE_HOST'"'

cp /default_settings.py /tmp/default_settings.py
sed "s/_ip_address_/$DATABASE_HOST/" /tmp/default_settings.py > \
/tmp/default_settings.py_

# Replace password in application settings
sed "s/_password_/$PGPASSWORD/" /tmp/default_settings.py_ > \
/default_settings.py

test -d venv || virtualenv venv
echo 'Activating virtual environment'
source venv/bin/activate

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

echo $SQL_QUERIES | psql -U navitia -h $DATABASE_HOST chaos

honcho -d $PROJECT_DIR -f /Procfile.txt start

