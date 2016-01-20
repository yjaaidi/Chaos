"""add property and associate_disruption_property tables

Revision ID: d8c17355ee8
Revises: 13d8517e7528
Create Date: 2016-01-21 14:27:22.163042

"""

# revision identifiers, used by Alembic.
revision = 'd8c17355ee8'
down_revision = '13d8517e7528'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    op.create_table(
        'property',
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('id', postgresql.UUID(), nullable=False),
        sa.Column('client_id', postgresql.UUID(), nullable=False),
        sa.Column('key', sa.Text(), nullable=False),
        sa.Column('type', sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(['client_id'], [u'client.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'type',
            'key',
            'client_id',
            name='property_type_key_client_id_uc',
        )
    )

    op.create_table(
        'associate_disruption_property',
        sa.Column('value', sa.Text(), nullable=True),
        sa.Column('disruption_id', postgresql.UUID(), nullable=False),
        sa.Column('property_id', postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['disruption_id'], [u'disruption.id'], ),
        sa.ForeignKeyConstraint(['property_id'], [u'property.id'], ),
        sa.PrimaryKeyConstraint('disruption_id', 'property_id', 'value')
    )


def downgrade():
    op.drop_table('associate_disruption_property')
    op.drop_table('property')
