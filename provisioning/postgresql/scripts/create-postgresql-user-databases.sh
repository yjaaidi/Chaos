#!/bin/bash

# Create navitia user
echo 'Create navitia PostgreSQL user'
CREATE_USER_QUERY="CREATE ROLE navitia WITH UNENCRYPTED PASSWORD '$NAVITIA_PASSWORD'"
echo $CREATE_USER_QUERY | psql -U postgres
echo "ALTER ROLE navitia WITH LOGIN;" | psql -U postgres

# Create chaos databases ("chaos" and "chaos_testing") with navitia user as their respective owners
echo 'Create "chaos" and "chaos_testing" databases with "navitia" as their respective owners'

function create_db {
    createdb -O navitia -E UTF-8 --lc-ctype='en_US.UTF-8' --lc-collate='en_US.UTF-8' -T template0 $1
}

create_db chaos
create_db chaos_testing

