"""alter severity effects

Revision ID: 3e96b43b6306
Revises: 15efa48238d6
Create Date: 2015-02-02 10:42:37.406960

"""

# revision identifiers, used by Alembic.
revision = '3e96b43b6306'
down_revision = '15efa48238d6'

from alembic import op
import sqlalchemy as sa


new_options = ('no_service', 'reduced_service', 'significant_delays', 'detour', 'additional_service', 'modified_service', 'other_effect', 'unknown_effect', 'stop_moved')

old_type = sa.Enum('blocking', name='severity_effect')
new_type = sa.Enum(*new_options, name='severity_effect')
tmp_type = sa.Enum(*new_options, name='_severity_effect')


def upgrade():
    #store blocking severity ids
    blockingIds = getBlockingSeverities('blocking')
    op.execute('UPDATE severity SET effect = NULL')

    # Create a tempoary "_severity_effect" type, convert and drop the "old" type
    tmp_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE severity ALTER COLUMN effect TYPE _severity_effect USING effect::text::_severity_effect')
    old_type.drop(op.get_bind(), checkfirst=False)

    # Create and convert to the "new" severity_effect type
    new_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE severity ALTER COLUMN effect TYPE severity_effect USING effect::text::severity_effect')
    tmp_type.drop(op.get_bind(), checkfirst=False)

    # Convert 'blocking' effects into 'no_service'
    updateBlockingSeverityEffects(blockingIds, 'no_service')


def downgrade():

    #store blocking severity ids
    blockingIds = getBlockingSeverities('no_service')
    op.execute('UPDATE severity SET effect = NULL')

    # Create a tempoary "_severity_effect" type, convert and drop the "new" type
    tmp_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE severity ALTER COLUMN effect TYPE _severity_effect USING effect::text::_severity_effect')
    new_type.drop(op.get_bind(), checkfirst=False)

    # Create and convert to the "old" severity_effect type
    old_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE severity ALTER COLUMN effect TYPE severity_effect USING effect::text::severity_effect')
    tmp_type.drop(op.get_bind(), checkfirst=False)

    updateBlockingSeverityEffects(blockingIds, 'blocking')

def getBlockingSeverities(value):
    connection = op.get_bind()
    result = connection.execute("SELECT id FROM severity WHERE effect = '%s'" % (value))

    ids = []
    for row in result:
        ids.append(row['id'])

    return ids

def updateBlockingSeverityEffects(severityIds, value):
    connection = op.get_bind()
    for id in severityIds:
        connection.execute("UPDATE severity SET effect = '%s' WHERE id = '%s'" % (value, id))
