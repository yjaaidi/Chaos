"""update disruption_status enum with 'draft' value

Revision ID: 484225f46268
Revises: d8c17355ee8
Create Date: 2016-04-13 16:47:55.164380

"""

# revision identifiers, used by Alembic.
revision = '484225f46268'
down_revision = 'd8c17355ee8'

from alembic import op
import sqlalchemy as sa

new_options = ('published', 'archived', 'draft')

old_type = sa.Enum('published', 'archived', name='disruption_status')
new_type = sa.Enum(*new_options, name='disruption_status')
tmp_type = sa.Enum(*new_options, name='tmp_disruption_status')

disruption_table = sa.sql.table(
    'disruption', sa.Column('status', new_type, nullable=False)
)


def upgrade():
    tmp_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'DROP DEFAULT')
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'TYPE tmp_disruption_status '
               'USING status::text::tmp_disruption_status')
    old_type.drop(op.get_bind(), checkfirst=False)

    new_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'TYPE disruption_status '
               'USING status::text::disruption_status')
    tmp_type.drop(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'SET DEFAULT \'published\'')


def downgrade():
    op.execute(
        disruption_table.update().where(
            disruption_table.c.status == u'draft'
        ).values(status='published'))

    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'DROP DEFAULT')
    tmp_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'TYPE tmp_disruption_status '
               'USING status::text::tmp_disruption_status')

    new_type.drop(op.get_bind(), checkfirst=False)
    old_type.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'TYPE disruption_status '
               'USING status::text::disruption_status')

    tmp_type.drop(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE disruption ALTER COLUMN status '
               'SET DEFAULT \'published\'')
