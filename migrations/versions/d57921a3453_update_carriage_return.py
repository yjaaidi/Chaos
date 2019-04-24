"""Update carriage return on HTML messages

Revision ID: d57921a3453
Revises: cf4581a9123
Create Date: 2019-04-24 17:05:02

"""

# revision identifiers, used by Alembic.
revision = 'd57921a3453'
down_revision = 'cf4581a9123'

from alembic import op

def upgrade():
    op.execute('UPDATE message SET text = regexp_replace(text, E\'[\\\\n\\\\r]\', \'\', \'g\' ) \
                FROM channel \
                WHERE message.channel_id = channel.id AND channel.content_type = \'text/html\';')

def downgrade():
    # function needed but not necessary for downgrade this fix