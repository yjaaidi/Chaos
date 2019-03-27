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
    op.execute('update impact set send_notifications = false where notification_date is null')

def downgrade():
    # doing send_notifications = true isn't what we want so downgrade is empty
    pass
