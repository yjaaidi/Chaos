"""Index tables in order to improve the performance of WS OGV1

Revision ID: 4f2a5821f666
Revises: 2d8031cd6452
Create Date: 2021-06-01 09:02:26.964407

"""

# revision identifiers, used by Alembic.
revision = '4f2a5821f666'
down_revision = '2d8031cd6452'

from alembic import op

indexes_data = [
    {'name': 'client_client_code_idx',                      'table': 'client',                      'columns': ['client_code']  },
    {'name': 'disruption_created_at_idx',                   'table': 'disruption',                  'columns': ['created_at']   },
    {'name': 'disruption_client_id_idx',                    'table': 'disruption',                  'columns': ['client_id']    },
    {'name': 'category_name_idx',                           'table': 'category',                    'columns': ['name']         },
    {'name': 'applicationperiods_start_date_idx',           'table': 'application_periods',         'columns': ['start_date']   },
    {'name': 'applicationperiods_end_date_idx',             'table': 'application_periods',         'columns': ['end_date']     },
    {'name': 'associate_wording_cause_wording_id_idx',      'table': 'associate_wording_cause',     'columns': ['wording_id']   },
    {'name': 'associate_wording_cause_cause_id_idx',        'table': 'associate_wording_cause',     'columns': ['cause_id']     },
    {'name': 'message_channel_id_idx',                      'table': 'message',                     'columns': ['channel_id']   },
    {'name': 'channel_name_idx',                            'table': 'channel',                     'columns': ['name']         },
    {'name': 'wording_key_idx',                             'table': 'wording',                     'columns': ['key']          },
    {'name': 'cause_category_idx',                          'table': 'cause',                       'columns': ['category_id']  },
    {'name': 'associate_impact_pt_object_impact_id_idx',    'table': 'associate_impact_pt_object',  'columns': ['impact_id']    },
    {'name': 'pt_object_uri_idx',                           'table': 'pt_object',                   'columns': ['uri']          },
]


def upgrade():
    for index_data in indexes_data :
        create_non_unique_index_if_not_exists(index_data)


def downgrade():
    for index_data in indexes_data :
        remove_index(index_data)


def index_exists(name):
    connection = op.get_bind()
    result = connection.execute("SELECT exists(SELECT 1 from pg_indexes where indexname = '{}') as ix_exists;" .format(name)).first()
    return result.ix_exists


def create_non_unique_index_if_not_exists(index_data):
    index_name = index_data['name']
    if not index_exists(index_name):
        op.create_index(index_name, index_data['table'], index_data['columns'], 'public', unique=False)


def remove_index(index_data) :
    op.drop_index(index_data['name'], index_data['table'], 'public')
