"""Add send_notifications column to impact

Revision ID: 1d9478df414e
Revises: 11f1722d941f
Create Date: 2015-09-22 13:57:07.072673

"""

# revision identifiers, used by Alembic.
revision = '1d9478df414e'
down_revision = '11f1722d941f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.add_column('impact', sa.Column('send_notifications', sa.Boolean(), nullable=False, server_default='false'))

def downgrade():
    op.drop_column('impact', 'send_notifications')

