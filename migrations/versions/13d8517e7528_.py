"""add wordings in line_section object

Revision ID: 13d8517e7528
Revises: 1d9478df414e
Create Date: 2015-11-06 12:45:03.853771

"""

# revision identifiers, used by Alembic.
revision = '13d8517e7528'
down_revision = '1d9478df414e'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.create_table('associate_wording_line_section',
    sa.Column('wording_id', postgresql.UUID(), nullable=False),
    sa.Column('line_section_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['line_section_id'], ['line_section.id'], ),
    sa.ForeignKeyConstraint(['wording_id'], ['wording.id'], ),
    sa.PrimaryKeyConstraint('wording_id', 'line_section_id', name='wording_line_section_pk')
    )


def downgrade():
    op.drop_table('associate_wording_line_section')
