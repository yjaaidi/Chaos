"""Index tables in order to improve the performance of WS OGV1

Revision ID: 4f2a5821f666
Revises: 2d8031cd6452
Create Date: 2021-06-01 09:02:26.964407

"""

# revision identifiers, used by Alembic.
revision = '4f2a5821f666'
down_revision = '2d8031cd6452'

from alembic import op


def upgrade():
    op.create_index('client_client_code_idx', 'client', ['client_code'], 'public', unique=False)
    op.create_index('disruption_created_at_idx', 'disruption', ['created_at'], 'public', unique=False)
    op.create_index('disruption_client_id_idx', 'disruption', ['client_id'], 'public', unique=False)
    op.create_index('category_name_idx', 'category', ['name'], 'public', unique=False)
    op.create_index('applicationperiods_start_date_idx', 'application_periods', ['start_date'], 'public', unique=False)
    op.create_index('applicationperiods_end_date_idx', 'application_periods', ['end_date'], 'public', unique=False)
    op.create_index('associate_wording_cause_wording_id_idx', 'associate_wording_cause', ['wording_id'], 'public', unique=False)
    op.create_index('associate_wording_cause_cause_id_idx', 'associate_wording_cause', ['cause_id'], 'public', unique=False)
    op.create_index('message_channel_id_idx', 'message', ['channel_id'], 'public', unique=False)
    op.create_index('channel_name_idx', 'channel', ['name'], 'public', unique=False)
    op.create_index('wording_key_idx', 'wording', ['key'], 'public', unique=False)
    op.create_index('cause_category_idx', 'cause', ['category_id'], 'public', unique=False)
    op.create_index('associate_impact_pt_object_impact_id_idx', 'associate_impact_pt_object', ['impact_id'], 'public', unique=False)
    op.create_index('pt_object_uri_idx', 'pt_object', ['uri'], 'public', unique=False)


def downgrade():
    op.drop_index('client_client_code_idx', 'client', 'public')
    op.drop_index('disruption_created_at_idx', 'disruption', 'public')
    op.drop_index('disruption_client_id_idx', 'disruption', 'public')
    op.drop_index('category_name_idx', 'category', 'public')
    op.drop_index('applicationperiods_start_date_idx', 'application_periods', 'public')
    op.drop_index('applicationperiods_end_date_idx', 'application_periods', 'public')
    op.drop_index('associate_wording_cause_wording_id_idx', 'associate_wording_cause', 'public')
    op.drop_index('associate_wording_cause_cause_id_idx', 'associate_wording_cause', 'public')
    op.drop_index('message_channel_id_idx', 'message', 'public')
    op.drop_index('channel_name_idx', 'channel', 'public')
    op.drop_index('wording_key_idx', 'wording', 'public')
    op.drop_index('cause_category_idx', 'cause', 'public')
    op.drop_index('associate_impact_pt_object_impact_id_idx', 'associate_impact_pt_object', 'public')
    op.drop_index('pt_object_uri_idx', 'pt_object', 'public')
