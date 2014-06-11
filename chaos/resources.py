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

from flask import abort, current_app, request
import flask_restful
from flask_restful import fields, marshal_with, marshal, reqparse, types
import sqlalchemy
from chaos import models, db
from jsonschema import validate

import logging

__all__ = ['Disruptions']


class FieldDateTime(fields.Raw):
    def format(self, value):
        if value:
            return value.strftime('%Y-%m-%dT%H:%M:%SZ')
        else:
            return 'null'


disruption_fields = {'id': fields.Raw,
                     'reference': fields.Raw,
                     'note': fields.Raw,
                     'created_at': FieldDateTime,
                     'updated_at': FieldDateTime,
                     }


disruptions_fields = {'disruptions': fields.List(fields.Nested(disruption_fields))
                     }

one_disruption_fields = {'disruption': fields.Nested(disruption_fields)
                     }

#see http://json-schema.org/
disruptions_input_format = {'type': 'object',
                            'properties': {'reference': {'type': 'string'},
                                            'note': {'type': 'string'},
                                        }
        }

class Disruptions(flask_restful.Resource):

    @marshal_with(disruptions_fields)
    def get(self):
        return {'disruptions': models.Disruption.query.all()}

    @marshal_with(one_disruption_fields)
    def post(self):
        json = request.get_json()
        logging.getLogger(__name__).debug(json)
        validate(json, disruptions_input_format)

        disruption = models.Disruption()
        disruption.reference = json['reference']
        disruption.note = json['note']
        db.session.add(disruption)
        db.session.commit()

        return {'disruption': disruption}
