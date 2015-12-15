#!/bin/bash

# Create navitia user
echo 'Create navitia PostgreSQL user'
CREATE_USER_QUERY="CREATE ROLE navitia WITH UNENCRYPTED PASSWORD '$NAVITIA_PASSWORD'"
echo $CREATE_USER_QUERY | psql -U postgres
echo "ALTER ROLE navitia WITH LOGIN;" | psql -U postgres

# Create chaos databases ("chaos" and "chaos_testing") with navitia user as their respective owners
echo 'Create "chaos" and "chaos_testing" databases with "navitia" as their respective owners'
createdb -O navitia chaos
createdb -O navitia chaos_testing
