# Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of Navitia,
#     the software to build cool stuff with public transport.
#
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


from functools import wraps
from chaos.navitia import Navitia
from utils import get_client_code, get_contributor_code, get_token, get_coverage
from chaos import exceptions, models, utils, fields
from flask_restful import marshal
from flask import request, current_app


class validate_client(object):
    def __init__(self, create_client=False):
        self.create_client = create_client

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                client_code = get_client_code(request)
            except exceptions.HeaderAbsent, e:
                return marshal({'error': {'message': utils.parse_error(e)}},
                               fields.error_fields), 400
            if self.create_client:
                client = models.Client.get_or_create(client_code)
            else:
                client = models.Client.get_by_code(client_code)
            if not client:
                return marshal({'error': {'message': 'X-Customer-Id {} Not Found'.format(client_code)}},
                               fields.error_fields), 404
            return func(*args, client=client, **kwargs)
        return wrapper


class validate_contributor(object):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                contributor_code = get_contributor_code(request)
            except exceptions.HeaderAbsent, e:
                return marshal({'error': {'message': utils.parse_error(e)}},
                               fields.error_fields), 400
            contributor = models.Contributor.get_by_code(contributor_code)
            if not contributor:
                return marshal({'error': {'message': 'X-Contributors {} Not Found'.format(contributor_code)}},
                               fields.error_fields), 404
            return func(*args, contributor=contributor, **kwargs)
        return wrapper


class validate_navitia(object):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                coverage = get_coverage(request)
                token = get_token(request)
            except exceptions.HeaderAbsent, e:
                return marshal({'error': {'message': utils.parse_error(e)}},
                               fields.error_fields), 400
            nav = Navitia(current_app.config['NAVITIA_URL'], coverage, token)
            return func(*args, navitia=nav, **kwargs)
        return wrapper

class manage_navitia_error(object):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions.NavitiaError, e:
                return marshal({'error': {'message': '{}'.format(e.message)}}, fields.error_fields), 503
        return wrapper
