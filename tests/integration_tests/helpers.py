
import chaos

import flask_migrate
from flask_migrate import Migrate
migrate = Migrate(chaos.app, chaos.db)

def setup_db():
    with chaos.app.app_context():
        flask_migrate.upgrade()

def teardown_db():
    with chaos.app.app_context():
        flask_migrate.downgrade(revision='base')
