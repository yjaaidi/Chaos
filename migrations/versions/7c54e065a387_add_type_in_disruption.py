"""Adding column type on disruption in order to have unexpected disruption

Revision ID: 7c54e065a387
Revises: 4f2a5821f666
Create Date: 2021-06-08 16:28:32.432146

"""

# revision identifiers, used by Alembic.
revision = '7c54e065a387'
down_revision = '4f2a5821f666'

from alembic import op
import sqlalchemy as sa

disruption_type_enum = sa.Enum('unexpected', name='disruption_type_enum')

def upgrade():
    disruption_type_enum.create(op.get_bind(), True)
    op.add_column('disruption', sa.Column('type', disruption_type_enum, nullable=True))


def downgrade():
    op.drop_column('disruption', 'type')
    disruption_type_enum.drop(op.get_bind())
