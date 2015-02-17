"""Add a new column client_id in the tables channel, cause and tag

Revision ID: 49de30166071
Revises: 3775ac5a659f
Create Date: 2014-11-26 14:05:59.823204

"""

# revision identifiers, used by Alembic.
revision = '49de30166071'
down_revision = '3775ac5a659f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channel', sa.Column('client_id', postgresql.UUID(), sa.ForeignKey('client.id')))
    op.add_column('cause', sa.Column('client_id', postgresql.UUID(), sa.ForeignKey('client.id')))
    op.add_column('tag', sa.Column('client_id', postgresql.UUID(), sa.ForeignKey('client.id')))
    connection = op.get_bind()
    result = connection.execute("select id from client where client_code = '{}'".format('trans'))
    row = result.first()
    if row and row['id']:
        op.execute("update channel set client_id='{}'".format(row['id']))
        op.execute("update cause set client_id='{}'".format(row['id']))
        op.execute("update tag set client_id='{}'".format(row['id']))

    op.execute("ALTER TABLE channel ALTER COLUMN client_id SET NOT NULL")
    op.execute("ALTER TABLE cause ALTER COLUMN client_id SET NOT NULL")
    op.execute("ALTER TABLE tag ALTER COLUMN client_id SET NOT NULL")
    op.execute("ALTER TABLE tag DROP CONSTRAINT tag_name_key")
    op.execute("ALTER TABLE tag ADD CONSTRAINT tag_name_client_id_key UNIQUE (name, client_id)")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channel', 'client_id')
    op.drop_column('cause', 'client_id')
    op.drop_column('tag', 'client_id')
    ### end Alembic commands ###