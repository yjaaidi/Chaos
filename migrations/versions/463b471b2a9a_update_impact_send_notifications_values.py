"""update impact send_notifications values

Revision ID: 463b471b2a9a
Revises: dfe97c5974e3
Create Date: 2019-03-22 12:19:48.562886

"""

# revision identifiers, used by Alembic.
revision = '463b471b2a9a'
down_revision = 'dfe97c5974e3'

from alembic import op


def upgrade():
    op.execute('UPDATE impact SET notification_date = COALESCE(updated_at, created_at) WHERE send_notifications = true AND notification_date IS null')

def downgrade():
    pass
