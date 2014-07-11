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

import requests
import logging

__all__ = ['Navitia']

class Navitia(object):
    def __init__(self, url, coverage, token=None, timeout=1):
        self.url = url
        self.coverage = coverage
        self.token = token
        self.timeout = timeout

    def get_network(self, uri):
        query = '{url}/v1/coverage/{coverage}/networks/{uri}'.format(
                url=self.url, coverage=self.coverage, uri=uri)
        try:
            response = requests.get(query, auth=(self.token, None), timeout=self.timeout)
        except (requests.exceptions.RequestException):
            logging.getLogger(__name__).exception('call to navitia failed')
            #currently we reraise the previous exceptions
            raise

        if response:
            json = response.json()
            if 'networks' in json and json['networks']:
                return json['networks'][0]

        return None



