"""Add some indexes

Revision ID: d3eacac50a6
Revises: 2cd4af730af5
Create Date: 2016-12-21 15:44:09.138657

"""

# revision identifiers, used by Alembic.
revision = 'd3eacac50a6'
down_revision = '2cd4af730af5'

from alembic import op


def upgrade():
    op.create_index('ix_disruption_contrib_status', 'disruption', ['contributor_id', 'status'], unique=False)
    op.create_index('ix_impact_disruption_status', 'impact', ['disruption_id', 'status'], unique=False)


def downgrade():
    op.drop_index('ix_disruption_contrib_status')
    op.drop_index('ix_impact_disruption_status')
