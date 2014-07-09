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

from flask import url_for, g
from functools import wraps
from datetime import datetime
from aniso8601 import parse_datetime

#disruption_id=None
def make_pager(resultset, endpoint, **kwargs):
    prev_link = None
    next_link = None
    last_link = None
    first_link = None

    if resultset.has_prev:
        prev_link = url_for(endpoint,
                            start_page=resultset.prev_num,
                            items_per_page=resultset.per_page,
                            _external=True, **kwargs)

    if resultset.has_next:
        next_link= url_for(endpoint,
                           start_page=resultset.next_num,
                           items_per_page=resultset.per_page,
                           _external=True, **kwargs)

    if resultset.total > 0:
        last_link= url_for(endpoint,
                       start_page=resultset.pages,
                       items_per_page=resultset.per_page,
                       _external=True, **kwargs)
        first_link = url_for(endpoint,
                         start_page=1,
                         items_per_page=resultset.per_page,
                         _external=True, **kwargs)

    result = {}
    result["pagination"] = {
                "start_page": resultset.page,
                "items_on_page": len(resultset.items),
                "items_per_page": resultset.per_page,
                "total_result": resultset.total,
                "prev": {"href": prev_link},
                "next": {"href": next_link},
                "first": {"href": first_link},
                "last": {"href": last_link
                }
    }
    return result


class paginate(object):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            page_index = kwargs['page_index']
            items_per_page = kwargs['items_per_page']
            del kwargs['page_index']
            del kwargs['items_per_page']
            objects = func(*args, **kwargs)
            result = objects.paginate(page_index, items_per_page)
            return result
        return wrapper


def get_datetime(value, name):
    """
        Convert string to datetime

        :param value: string to convert
        :param name: attribute name
        :return: DateTime format '2014-04-31T16:52:00'
        tzinfo=None : information about the offset from UTC time
    """
    try:
        return parse_datetime(value).replace(tzinfo=None)
    except:
        raise ValueError("The {} argument value is not valid, you gave: {}"
                         .format(name, value))


def get_current_time():
    """
        Get current time global variable
        :return: DateTime format '2014-04-31T16:52:00'
    """
    if 'current_time' in g and g.current_time:
        return g.current_time
    else:
        return datetime.utcnow()

def option_value(values):
    def to_return(value, name):
        if not value in values:
            error = "The {} argument must be in list {}, you gave {}".\
                format(name, str(values), value)
            raise ValueError(error)
        return value
    return to_return

