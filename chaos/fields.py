# Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of Navitia,
#     the software to build cool stuff with public transport.
#
# Hope you'll enjoy and contribute to this project,
#     powered by Canal TP (www.canaltp.fr).
# Help us simplify mobility and open public transport:
#     a non ending quest to the responsive locomotion way of traveling!
#
# LICENCE: This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Stay tuned using
# twitter @navitia
# IRC #navitia on freenode
# https://groups.google.com/d/forum/navitia
# www.navitia.io

from flask_restful import fields, url_for
from flask import current_app
from  utils import make_pager
from chaos.navitia import Navitia

class FieldDateTime(fields.Raw):
    def format(self, value):
        if value:
            return value.strftime('%Y-%m-%dT%H:%M:%SZ')
        else:
            return 'null'


class FieldPaginateImpacts(fields.Raw):
    '''
    Pagination of impacts list for one disruption
    '''
    def output(self, key, disruption):
        return make_pager(disruption.impacts.paginate(1, 20), 'impact', disruption_id=disruption.id)

class FieldUrlDisruption(fields.Raw):
    def output(self, key, obj):
        return {'href': url_for('disruption', id=obj.disruption_id, _external=True)}

class FieldObjectName(fields.Raw):
    def output(self, key, obj):
        navitia = Navitia(current_app.config['NAVITIA_URL'],
                               current_app.config['NAVITIA_COVERAGE'],
                               current_app.config['NAVITIA_TOKEN'])
        response = navitia.get_network(obj.uri)
        if response and 'name' in response:
            return response['name']
        return 'Unable to find object'


href_field = {
    "href": fields.String
}

disruption_fields = {'id': fields.Raw,
                     'self': {'href': fields.Url('disruption', absolute=True)},
                     'reference': fields.Raw,
                     'note': fields.Raw,
                     'status': fields.Raw,
                     'created_at': FieldDateTime,
                     'updated_at': FieldDateTime,
                     'publication_period': {
                            'begin': FieldDateTime(attribute='start_publication_date'),
                            'end': FieldDateTime(attribute='end_publication_date'),
                         },
                     'publication_status': fields.Raw,
                     'impacts': FieldPaginateImpacts(attribute='impacts')
}

paginate_fields = {
        "start_page": fields.String,
        "items_on_page": fields.String,
        "items_per_page": fields.String,
        "total_result": fields.String,
        "prev": fields.Nested(href_field),
        "next": fields.Nested(href_field),
        "first": fields.Nested(href_field),
        "last": fields.Nested(href_field)
}

meta_fields = {
    "pagination": fields.Nested(paginate_fields)
}

disruptions_fields = {"meta": fields.Nested(meta_fields),
                      "disruptions": fields.List(fields.Nested(disruption_fields))
                    }

one_disruption_fields = {'disruption': fields.Nested(disruption_fields)
                        }

error_fields = {'error': fields.Nested({'message': fields.String})}


severity_fields = {'id': fields.Raw,
                   'wording': fields.Raw,
                   'color': fields.Raw,
                   'created_at': FieldDateTime,
                   'updated_at': FieldDateTime,
                   'self': {'href': fields.Url('severity', absolute=True)},
                   'priority': fields.Integer(default=None),
                   'effect': fields.Raw(),
}

severities_fields = {'severities': fields.List(fields.Nested(severity_fields)),
                     'meta': {},
}

one_severity_fields = {'severity': fields.Nested(severity_fields)
                        }

cause_fields = {'id': fields.Raw,
                   'wording': fields.Raw,
                   'created_at': FieldDateTime,
                   'updated_at': FieldDateTime,
                   'self': {'href': fields.Url('cause', absolute=True)},
}

causes_fields = {'causes': fields.List(fields.Nested(cause_fields)),
                     'meta': {},
}

one_cause_fields = {'cause': fields.Nested(cause_fields)
                        }

objectTC_fields = {'id': fields.Raw(attribute='uri'),
                   'type': fields.Raw,
                   'name': FieldObjectName()
}

application_period_fields = {
    'begin': FieldDateTime(attribute='start_date'),
    'end': FieldDateTime(attribute='end_date')
}

class FieldMessage(fields.Raw):
    def output(self, key, obj):
        result = []
        result.append( {"id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                        "created_at": "2014-04-31T16:52:18Z",
                        "updated_at": "2014-04-31T16:55:18Z",
                        "text": "ptit dej a la gare!!"})
        result[0]["channel"] = {}
        result[0]["channel"]["id"] = "3d1f42b2-e8df-11e3-8c3e-0008ca8657da"
        result[0]["channel"]["name"] = "message court"
        result[0]["channel"]["content_type"] = "text/plain"
        result[0]["channel"]["created_at"] = "2014-04-31T16:52:18Z"
        result[0]["channel"]["updated_at"] = "updated_at"
        result[0]["channel"]["max_size"] = 150

        return result



impact_fields = {'id': fields.Raw,
                 'created_at': FieldDateTime,
                 'updated_at': FieldDateTime,
                 'objects': fields.List(fields.Nested(objectTC_fields)),
                 'application_periods': fields.List(fields.Nested(application_period_fields)),
                 'severity': fields.Nested(severity_fields),
				 'self': {'href': fields.Url('impact', absolute=True)},
                 'disruption': FieldUrlDisruption(),
                 'messages':FieldMessage
}

one_impact_fields = {'impact': fields.Nested(impact_fields)

}

impacts_fields = {'meta': fields.Nested(meta_fields),
                  'impacts': fields.List(fields.Nested(impact_fields))
}

channel_fields = {'id': fields.Raw,
                   'name': fields.Raw,
                   'max_size': fields.Integer(default=None),
                   'content_type': fields.Raw,
                   'created_at': FieldDateTime,
                   'updated_at': FieldDateTime,
                   'self': {'href': fields.Url('channel', absolute=True)}
}

channels_fields = {'channels': fields.List(fields.Nested(channel_fields)),
                     'meta': {},
}


one_channel_fields = {'channel': fields.Nested(channel_fields)
}

#Mock response impacts API

object_fields = {
    "id": "RER:A",
    "name": "RER:A",
    "type": "network",
    "impacts": [
        {
            "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ea",
            "self": {"href": "https://chaos.apiary-mock.com/disruptions/3d1f32b2-e8df-11e3-8c3e-0008ca8657ea/impacts/3d1f42b2-e8df-11e3-8c3e-0008ca8657ea"},
              "created_at": "2014-04-31T16:52:18Z",
              "updated_at": "2014-04-31T16:55:18Z",
              "severity": {
                  "id": "3d1f42b2-e8df-11e3-8c3e-0008ca86c7ea",
                  "wording": "Bonne nouvelle",
                  "created_at": "2014-04-31T16:52:18Z",
                  "updated_at": "2014-04-31T16:55:18Z",
                  "color": "#123456",
                  "effect": None
              },
              "application_periods": [
                  {
                      "begin": "2014-03-29T16:52:00Z",
                      "end": "2014-05-22T02:15:00Z"
                  }
              ],
                            "messages": [
                  {
                      "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657ca",
                      "created_at": "2014-04-31T16:52:18Z",
                      "updated_at": "2014-04-31T16:55:18Z",
                      "text": "ptit dej la gare!!",
                      "channel": {
                          "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8657da",
                          "name": "message court",
                          "content_type": "text/plain",
                          "created_at": "2014-04-31T16:52:18Z",
                          "updated_at": "2014-04-31T16:55:18Z",
                          "max_size": 140
                      }
                  },
                  {
                      "id": "3d1f42b2-e8df-11e3-8c3e-0008ca8257ea",
                      "created_at": "2014-04-31T16:52:18Z",
                      "updated_at": "2014-04-31T16:55:18Z",
                      "text": "est ptit dej en gare",
                      "channel": {
                          "id": "3d1f42b2-e8df-11e3-8c3e-0008cb8657ea",
                          "name": "message long",
                          "content_type": "text/markdown",
                          "created_at": "2014-04-31T16:52:18Z",
                          "updated_at": "2014-04-31T16:55:18Z",
                          "max_size": None
                      }
                  }
              ],
              "object": [{
        "id":"RER:A",
        "name": "RER:A",
        "type": "network"
      }]
        }
    ]
}

objects_fields = { 'objects': [object_fields] }
