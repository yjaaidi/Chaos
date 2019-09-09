"""Add author of disruption

Revision ID: 4e3c651ba4be
Revises: 50f90e14e248
Create Date: 2019-08-30 12:25:57.136650

"""

# revision identifiers, used by Alembic.
revision = '4e3c651ba4be'
down_revision = '50f90e14e248'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('disruption', sa.Column('author', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('disruption', 'author')
