#!/bin/bash

# Wait for the database to be online
# See also https://github.com/docker/compose/issues/374
sleep 10

DATABASE_HOST='chaos_database'
PROJECT_DIR=/var/www/chaos

cd $PROJECT_DIR

echo 'PostgreSQL database will listen on port port 5432 of host "'$DATABASE_HOST'"'

cp /default_settings.py /tmp/default_settings.py

# Replace IP address and password in application settings
sed -e "s/_password_/$PGPASSWORD/" -e "s/_ip_address_/$DATABASE_HOST/" /tmp/default_settings.py > \
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

cp /testing_settings.py $PROJECT_DIR/tests

echo $SQL_QUERIES | psql -U navitia -h $DATABASE_HOST chaos

if [ -e $PROJECT_DIR/.env ]
then
    echo 'Your environment configuration file will be move to comply with docker use requirements'
    mv $PROJECT_DIR/.env $PROJECT_DIR/.`date +"%Y%d%m_%H_%M"`_env
fi

honcho -d $PROJECT_DIR -f /Procfile.txt start

