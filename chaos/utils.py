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
import uuid
import flask


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
        next_link = url_for(endpoint,
                            start_page=resultset.next_num,
                            items_per_page=resultset.per_page,
                            _external=True, **kwargs)

    if resultset.total > 0:
        last_link = url_for(endpoint,
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
        "last": {"href": last_link}
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


class Request(flask.Request):
    """
    override the request of flask to add an id on all request
    """
    def __init__(self, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)
        self.id = str(uuid.uuid4())


def is_pt_object_valid(pt_object, object_type, uris):
    """
    verification object by its type and uri
    :param pt_object: public transport object
    :param object_type: public transport object type
    :param uris: public transport object uri
    :return: bool
    """
    if object_type:
        if uris:
            return ((pt_object.type == object_type) and
                    (pt_object.uri in uris))
        else:
            return (pt_object.type == object_type)
    elif uris:
        return (pt_object.uri in uris)
    else:
        return False


def group_impacts_by_pt_object(impacts, object_type, uris, get_pt_object):
    """
    :param impacts: list of impacts
    :param object_type: PTObject type example stop_area
    :return: list of implacts group by PTObject sorted by name
    """
    dictionary = {}
    for impact in impacts:
        for pt_object in impact.objects:
            if is_pt_object_valid(pt_object, object_type, uris):
                if pt_object.uri in dictionary:
                    resp = dictionary[pt_object.uri]
                else:
                    nav_pt_object = get_pt_object(pt_object.uri, pt_object.type)
                    if nav_pt_object and 'name' in nav_pt_object:
                        name = nav_pt_object['name']
                    else:
                        name = None
                    resp = {'id': pt_object.uri,
                            'type': pt_object.type,
                            'name': name,
                            'impacts': []
                    }
                    dictionary[pt_object.uri] = resp
                resp['impacts'].append(impact)
    result = dictionary.values()
    result.sort(key=lambda x: x['name'])
    return result


def parse_error(error):
    to_return = None
    try:
        to_return = error.message
    except AttributeError:
        to_return = str(error).replace("\n", " ")
    return to_return
