"""add indexes on line_section

Revision ID: 458134a1e5ea
Revises: e33962db5d9
Create Date: 2017-07-20 10:17:15.224515

"""

# revision identifiers, used by Alembic.
revision = '458134a1e5ea'
down_revision = 'e33962db5d9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('ix_line_section_object_id', 'line_section', ['object_id'], unique=False)


def downgrade():
    op.drop_index('ix_line_section_object_id')
