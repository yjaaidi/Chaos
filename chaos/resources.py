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

from flask import request, url_for, g
import flask_restful
from flask_restful import marshal, reqparse
from chaos import models, db
from jsonschema import validate, ValidationError
from flask.ext.restful import abort
from fields import *
from formats import disruptions_input_format, publication_status_values, severity_input_format, id_format
from chaos import mapper
from chaos import utils

import logging
from utils import make_pager, option_value

__all__ = ['Disruptions']


disruption_mapping = {'reference': None,
        'note': None,
        'publication_period': {
            'begin': mapper.Datetime(attribute='start_publication_date'),
            'end': mapper.Datetime(attribute='end_publication_date')
            }
        }

severity_mapping = {'wording': None,
                    'color': None,
                    'priority': None,
                    'effect': None,
}

class Index(flask_restful.Resource):

    def get(self):
        url = url_for('disruption', _external=True)
        response = {
            "disruptions": {"href": url},
            "disruption": {"href": url + '/{id}', "templated": True},
            "severities": {"href": url_for('severity', _external=True)},
        }
        return response, 200

class Severity(flask_restful.Resource):

    def get(self, id=None):
        if id:
            if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
            response = {'severity': models.Severity.get(id)}
            return marshal(response, one_severity_fields)
        else:
            response = {'severities': models.Severity.all(), 'meta': {}}
            return marshal(response, severities_fields)

    def post(self):
        json = request.get_json()
        logging.getLogger(__name__).debug('Post severity: %s', json)
        try:
            validate(json, severity_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        severity = models.Severity()
        mapper.fill_from_json(severity, json, severity_mapping)
        db.session.add(severity)
        db.session.commit()
        return marshal({'severity': severity}, one_severity_fields), 201

    def put(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                    error_fields), 400
        severity = models.Severity.get(id)
        json = request.get_json()
        logging.getLogger(__name__).debug('PUT severity: %s', json)

        try:
            validate(json, severity_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        mapper.fill_from_json(severity, json, severity_mapping)
        db.session.commit()
        return marshal({'severity': severity}, one_severity_fields), 200

    def delete(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        severity = models.Severity.get(id)
        severity.is_visible = False
        db.session.commit()
        return None, 204


class Disruptions(flask_restful.Resource):
    def __init__(self):
        self.parsers = {}
        self.parsers["get"] = reqparse.RequestParser()
        parser_get = self.parsers["get"]

        parser_get.add_argument("start_page", type=int, default=1)
        parser_get.add_argument("items_per_page", type=int, default=20)
        parser_get.add_argument("publication_status[]", type=option_value(publication_status_values), action="append", default=publication_status_values)
        parser_get.add_argument("current_time", type=utils.get_datetime)



    def get(self, id=None):
        if id:
            if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                               error_fields), 400
            return marshal({'disruption': models.Disruption.get(id)},
                           one_disruption_fields)
        else:
            args = self.parsers['get'].parse_args()
            page_index = args['start_page']
            if page_index == 0:
                abort(400, message="page_index argument value is not valid")
            items_per_page = args['items_per_page']
            if items_per_page == 0:
                abort(400, message="items_per_page argument value is not valid")
            publication_status = args['publication_status[]']
            g.current_time = args['current_time']
            result = models.Disruption.all_with_filter(page_index=page_index, items_per_page=items_per_page, publication_status=publication_status)
            response = {'disruptions': result.items, 'meta': make_pager(result, 'disruption')}
            return marshal(response, disruptions_fields)

    def post(self):
        json = request.get_json()
        logging.getLogger(__name__).debug(json)
        try:
            validate(json, disruptions_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), \
                    400

        disruption = models.Disruption()
        mapper.fill_from_json(disruption, json, disruption_mapping)
        db.session.add(disruption)
        db.session.commit()
        return marshal({'disruption': disruption}, one_disruption_fields), 201


    def put(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        disruption = models.Disruption.get(id)
        json = request.get_json()
        logging.getLogger(__name__).debug(json)

        try:
            validate(json, disruptions_input_format)
        except ValidationError, e:
            logging.getLogger(__name__).debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), \
                    400

        mapper.fill_from_json(disruption, json, disruption_mapping)
        db.session.commit()
        return marshal({'disruption': disruption}, one_disruption_fields), 200

    def delete(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        disruption = models.Disruption.get(id)
        disruption.archive()
        db.session.commit()
        return None, 204
