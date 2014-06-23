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

from flask import url_for
from functools import wraps


def format_url(endpoint, start_index, per_page):
    return url_for(endpoint,
                   start_page=start_index,
                   items_per_page=per_page,
                   _external=True)

class make_pager(object):

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            objects = f(*args, **kwargs)
            prev = None
            next = None
            if objects.has_prev:
                prev = format_url('disruption', objects.prev_num, objects.per_page)

            if objects.has_next:
                next = format_url('disruption', objects.next_num, objects.per_page)

            last = format_url('disruption', objects.pages, objects.per_page)

            first = format_url('disruption', 1, objects.per_page)
            result = {}
            result["disruptions"] = objects.items
            result["meta"] = {
                "pagination":{
                        "start_page": objects.page,
                        "items_on_page": len(objects.items),
                        "items_per_page": objects.per_page,
                        "total_result": objects.total,
                        "prev": {"href": prev},
                        "next": {"href": next},
                        "first": {"href": first},
                        "last": {"href": last}
                }
            }
            return result
        return wrapper
