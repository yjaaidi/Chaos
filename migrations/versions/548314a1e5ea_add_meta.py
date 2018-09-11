"""add meta

Revision ID: 548314a1e5ea
Revises: 458134a1e5ea
Create Date: 2018-09-11 14:17:15.224515

"""

# revision identifiers, used by Alembic.
revision = '548314a1e5ea'
down_revision = '458134a1e5ea'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.create_table('meta',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('key', sa.Text(), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='meta_pk')
    )
    op.create_table('associate_message_meta',
    sa.Column('message_id', postgresql.UUID(), nullable=False),
    sa.Column('meta_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.ForeignKeyConstraint(['meta_id'], ['meta.id'], ),
    sa.PrimaryKeyConstraint('message_id', 'meta_id', name='message_meta_pk')
    )


def downgrade():
    op.drop_table('associate_message_meta')
    op.drop_table('meta')
