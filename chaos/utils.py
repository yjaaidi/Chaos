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


def format_url(endpoint, start_index, per_page):
    return url_for(endpoint,
                   start_page=start_index,
                   count=per_page,
                   _external=True)

def get_meta(result):

    prev = None
    next = None
    if result.has_prev:
        prev = format_url('disruption', result.prev_num, result.per_page)

    if result.has_next:
        next = format_url('disruption', result.next_num, result.per_page)

    last = format_url('disruption', result.pages, result.per_page)

    first = format_url('disruption', 1, result.per_page)

    return {
        "pagination": {
        "start_page": result.page,
        "items_on_page": len(result.items),
        "items_per_page": result.per_page,
        "total_result": result.total,
        "prev": {"href": prev},
        "next": {"href": next},
        "first": {"href": first},
        "last": {"href": last}
        }
    }
