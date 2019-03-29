"""Create export table

Revision ID: bf4581a9122
Revises: 143e661e5114
Create Date: 2019-03-20 16:59:47.907869

"""

# revision identifiers, used by Alembic.
revision = 'bf4581a9122'
down_revision = 'dfe97c5974e3'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

status_type = sa.Enum('waiting', 'handling', 'error', 'done', name='status')

def upgrade():
    op.create_table('export',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('client_id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('process_start_date', sa.DateTime(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], [u'client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    status_type.create(op.get_bind(), True)
    op.add_column('export', sa.Column('status', status_type, nullable=False, server_default='waiting'))


def downgrade():
    op.drop_table('export')
