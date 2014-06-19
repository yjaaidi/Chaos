from lettuce import *
import chaos
import logging
import json

import flask_migrate
from flask_migrate import Migrate
migrate = Migrate(chaos.app, chaos.db)


@before.each_scenario
def setup_db(scenario):
    logging.getLogger('alembic').setLevel(logging.ERROR)
    with chaos.app.app_context():
        flask_migrate.upgrade(directory='../migrations')

@before.each_scenario
def setup_tester(scenario):
    world.client = chaos.app.test_client()


@after.each_scenario
def teardown_db(scenario):
    with chaos.app.app_context():
        flask_migrate.downgrade(revision='base', directory='../migrations')
@before.each_step
def retrieve_json_response(step):
    if hasattr(world, 'response') and not hasattr(world, 'reponse_json'):
        world.response_json = json.loads(world.response.get_data())
