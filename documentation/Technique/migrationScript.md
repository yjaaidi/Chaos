# How to create a migration script
---------------------

Update your local database
---------------------
    honcho run ./manage.py db upgrade

Modify the models
---------------------
Change the model file (chaos/models.py) to add, update or delete columns

Generate the migration script from models automatically
---------------------
    honcho run ./manage.py db migrate
With this command, a migration script will be created in the directory migrations/versions/.
This script is generated from the different between the model file and your local database.

Modify the script
---------------------
Modify the first line to a understandable title.
This script generated automatically may have some useless elements, you can remove them and keep useful elements only

Test the script
---------------------
To apply changes to the database:

    honcho run ./manage.py db upgrade

To remove changes from the database:

    honcho run ./manage.py db downgrade
