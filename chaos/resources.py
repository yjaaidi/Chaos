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

from flask import request, url_for, g, current_app
import flask_restful
from flask_restful import marshal, reqparse
from chaos import models, db
from jsonschema import validate, ValidationError
from flask.ext.restful import abort
from fields import *
from formats import *
from formats import impact_input_format, channel_input_format
from chaos import mapper
from chaos import utils
import chaos
from chaos.navitia import Navitia

import logging
from utils import make_pager, option_value

__all__ = ['Disruptions', 'Index', 'Severity', 'Cause']


disruption_mapping = {'reference': None,
        'note': None,
        'publication_period': {
            'begin': mapper.Datetime(attribute='start_publication_date'),
            'end': mapper.Datetime(attribute='end_publication_date')
            },
        'cause': {'id': mapper.AliasText(attribute='cause_id')},
        'localization':[{"id":mapper.Localization(attribute='localization_id')}]
        }

severity_mapping = {'wording': None,
                    'color': None,
                    'priority': None,
                    'effect': None,
}

cause_mapping = {'wording': None,}

object_mapping = {
    "id": mapper.AliasText(attribute='uri'),
    "type": None
}

application_period_mapping = {
    'begin': mapper.Datetime(attribute='start_date'),
    'end': mapper.Datetime(attribute='end_date')
}

channel_mapping = {'name': None,
                    'max_size': None,
                    'content_type': None
}

class Index(flask_restful.Resource):

    def get(self):
        url = url_for('disruption', _external=True)
        response = {
            "disruptions": {"href": url},
            "disruption": {"href": url + '/{id}', "templated": True},
            "severities": {"href": url_for('severity', _external=True)},
            "causes": {"href": url_for('cause', _external=True)},
            "channels": {"href": url_for('channel', _external=True)},
            "impactsbyobject": {"href": url_for('impactsbyobject', _external=True)}
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
        self.navitia = Navitia(current_app.config['NAVITIA_URL'],
                               current_app.config['NAVITIA_COVERAGE'],
                               current_app.config['NAVITIA_TOKEN'])
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

        #Add localization present in Json
        if 'localization' in json and json['localization']:
            if not self.navitia.get_pt_object(disruption.localization_id, json['localization'][0]["type"]):
                        return marshal({'error': {'message': 'ptobject {} doesn\'t exist'.format(disruption.localization_id)}},
                            error_fields), 404
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

        #Add localization present in Json
        if 'localization' in json and json['localization']:
            if not self.navitia.get_pt_object(disruption.localization_id, json['localization'][0]["type"]):
                    return marshal({'error': {'message': 'ptobject {} doesn\'t exist'.format(disruption.localization_id)}},
                            error_fields), 404

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

class Cause(flask_restful.Resource):

    def get(self, id=None):
        if id:
            if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
            response = {'cause': models.Cause.get(id)}
            return marshal(response, one_cause_fields)
        else:
            response = {'causes': models.Cause.all(), 'meta': {}}
            return marshal(response, causes_fields)

    def post(self):
        json = request.get_json()
        logging.getLogger(__name__).debug('Post cause: %s', json)
        try:
            validate(json, cause_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        cause = models.Cause()
        mapper.fill_from_json(cause, json, cause_mapping)
        db.session.add(cause)
        db.session.commit()
        return marshal({'cause': cause}, one_cause_fields), 201

    def put(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                    error_fields), 400
        cause = models.Cause.get(id)
        json = request.get_json()
        logging.getLogger(__name__).debug('PUT cause: %s', json)

        try:
            validate(json, cause_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        mapper.fill_from_json(cause, json, cause_mapping)
        db.session.commit()
        return marshal({'cause': cause}, one_cause_fields), 200

    def delete(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        cause = models.Cause.get(id)
        cause.is_visible = False
        db.session.commit()
        return None, 204

class ImpactsByObject(flask_restful.Resource):
    def get(self):
        return objects_fields

class Impacts(flask_restful.Resource):
    def __init__(self):
        self.navitia = Navitia(current_app.config['NAVITIA_URL'],
                               current_app.config['NAVITIA_COVERAGE'],
                               current_app.config['NAVITIA_TOKEN'])
        self.parsers = {}
        self.parsers["get"] = reqparse.RequestParser()
        parser_get = self.parsers["get"]

        parser_get.add_argument("start_page", type=int, default=1)
        parser_get.add_argument("items_per_page", type=int, default=20)

    def get(self, disruption_id, id=None):
        if id:
            if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
            response = models.Impact.get(id)
            return marshal({'impact': response},
                           one_impact_fields)
        else:
            if not id_format.match(disruption_id):
                return marshal({'error': {'message': "disruption_id invalid"}},
                           error_fields), 400
            args = self.parsers['get'].parse_args()
            page_index = args['start_page']
            if page_index == 0:
                abort(400, message="page_index argument value is not valid")
            items_per_page = args['items_per_page']
            if items_per_page == 0:
                abort(400, message="items_per_page argument value is not valid")

            result = models.Impact.all(page_index=page_index, items_per_page=items_per_page, disruption_id=disruption_id)
            response = {'impacts' : result.items, 'meta': make_pager(result, 'impact', disruption_id=disruption_id)}
            return marshal(response, impacts_fields)

    def post(self, disruption_id):
        if not id_format.match(disruption_id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400

        json = request.get_json()
        logging.getLogger(__name__).debug(json)

        try:
            validate(json, impact_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        impact = models.Impact()
        impact.severity = models.Severity.get(json['severity']['id'])

        impact.disruption_id = disruption_id
        db.session.add(impact)

        #Add all objects present in Json
        if json:
            if 'objects' in json:
                for obj in  json['objects']:
                    object = models.PTobject()
                    object.impact_id = impact.id
                    mapper.fill_from_json(object, obj, object_mapping)
                    if not self.navitia.get_pt_object(obj['id'], obj['type']):
                        return marshal({'error': {'message': 'network {} doesn\'t exist'.format(obj['id'])}},
                                       error_fields), 404
                    impact.insert_object(object)
            if 'application_periods' in json:
                for app_period in json["application_periods"]:
                    application_period = models.ApplicationPeriods(impact.id)
                    mapper.fill_from_json(application_period, app_period, application_period_mapping)
                    impact.insert_app_period(application_period)

        db.session.commit()
        return marshal({'impact': impact}, one_impact_fields), 201

    def put(self, disruption_id, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        json = request.get_json()
        logging.getLogger(__name__).debug(json)
        impact = models.Impact.get(id)

        #Add all objects present in Json
        if json:
            if 'objects' in json:
                for obj in  json['objects']:
                    object = models.PTobject()
                    object.impact_id = impact.id
                    mapper.fill_from_json(object, obj, object_mapping)
                    if not self.navitia.get_pt_object(obj['id'], obj['type']):
                        return marshal({'error': {'message': 'network {} doesn\'t exist'.format(obj['id'])}},
                                error_fields), 404
                    impact.insert_object(object)
            if 'application_periods' in json:
                for app_period in json["application_periods"]:
                    application_period = models.ApplicationPeriods(impact.id)
                    mapper.fill_from_json(application_period, app_period, application_period_mapping)
                    impact.insert_app_period(application_period)

        db.session.commit()
        return marshal({'impact': impact}, one_impact_fields), 200

    def delete(self, disruption_id, id):
        if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                               error_fields), 400
        impact = models.Impact.get(id)
        impact.archive()
        db.session.commit()
        return None, 204

class Channel(flask_restful.Resource):

    def get(self, id=None):
        if id:
            if not id_format.match(id):
                return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
            response = {'channel': models.Channel.get(id)}
            return marshal(response, one_channel_fields)
        else:
            response = {'channels': models.Channel.all(), 'meta': {}}
            return marshal(response, channels_fields)

    def post(self):
        json = request.get_json()
        logging.getLogger(__name__).debug('Post channel: %s', json)
        try:
            validate(json, channel_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        channel = models.Channel()
        mapper.fill_from_json(channel, json, channel_mapping)
        db.session.add(channel)
        db.session.commit()
        return marshal({'channel': channel}, one_channel_fields), 201

    def put(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                    error_fields), 400
        channel = models.Channel.get(id)
        json = request.get_json()
        logging.getLogger(__name__).debug('PUT channel: %s', json)

        try:
            validate(json, channel_input_format)
        except ValidationError, e:
            logging.debug(str(e))
            #TODO: generate good error messages
            return marshal({'error': {'message': str(e).replace("\n", " ")}},
                           error_fields), 400

        mapper.fill_from_json(channel, json, channel_mapping)
        db.session.commit()
        return marshal({'channel': channel}, one_channel_fields), 200

    def delete(self, id):
        if not id_format.match(id):
            return marshal({'error': {'message': "id invalid"}},
                           error_fields), 400
        channel = models.Channel.get(id)
        channel.is_visible = False
        db.session.commit()
        return None, 204

class Status(flask_restful.Resource):
    def get(self):
        return {'version': chaos.VERSION,
                'db_pool_status': db.engine.pool.status(),
                'db_version': db.engine.scalar('select version_num from alembic_version;')}

