"""empty message

Revision ID: 2cd4af730af5
Revises: 484225f46268
Create Date: 2016-06-21 16:51:16.605602

"""

# revision identifiers, used by Alembic.
revision = '2cd4af730af5'
down_revision = '484225f46268'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.add_column('impact', sa.Column('version', sa.Integer(), nullable=False, server_default='1'))

def downgrade():
    op.drop_column('impact', 'version')
