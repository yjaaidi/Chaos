"""add channel required

Revision ID: dfe97c5974e3
Revises: 548314a1e5ea
Create Date: 2018-10-01 14:47:15.224515

"""

# revision identifiers, used by Alembic.
revision = 'dfe97c5974e3'
down_revision = '548314a1e5ea'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('channel', sa.Column('required', sa.Boolean(), nullable=False, server_default='false'))

def downgrade():
    op.drop_column('channel', 'required')
