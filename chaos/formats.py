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

__all__ = ['disruptions_input_format', 'publication_status_values',
           'severity_input_format', 'id_format', 'cause_input_format']
import re
#see http://json-schema.org/

datetime_pattern = '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'
id_format_text = '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
id_format = re.compile(id_format_text)
pt_object_type_values = ["network", "stop_area"]
#Here Order of values is strict and is used to create query filters.
publication_status_values = ["past", "ongoing", "coming"]

date_period_format = {
    'type': 'object',
    'properties': {
        'begin': {'type': ['string'], 'pattern': datetime_pattern},
        'end': {'type': ['string', 'null'], 'pattern': datetime_pattern},
        },
    'required': ['begin', 'end']
}

object_input_format = {
    'type': 'object',
    'properties': {'id': {'type': 'string', 'maxLength': 250},
                   'type': {'enum': pt_object_type_values}
    },
    'required': ['id', 'type']
}

localization_object_input_format = {
    'type': 'object',
    'properties': {'id': {'type': 'string', 'maxLength': 250},
                   'type': {'enum': ["stop_area"]}
    },
    'required': ['id', 'type']
}

disruptions_input_format = {
    'type': 'object',
    'properties': {'reference': {'type': 'string', 'maxLength': 250},
                   'note': {'type': 'string'},
                   'publication_period': date_period_format,
                   'cause': {
                       'type': 'object',
                       'properties': {
                           'id': {'type': 'string', 'pattern': id_format_text}
                       },
                       'required': ['id']
                   },
                   'localization': {'type': 'array',
                                    'items': [localization_object_input_format]
                   }
    },
    'required': ['reference', 'cause']
}

severity_input_format = {
    'type': 'object',
    'properties': {'wording': {'type': 'string', 'maxLength': 250},
                   'color': {'type': ['string', 'null'], 'maxLength': 20},
                   'priority': {'type': ['integer', 'null']},
                   'effect': {'enum': ['blocking', None]},
                   },
    'required': ['wording']
}

cause_input_format = {
    'type': 'object',
    'properties': {'wording': {'type': 'string', 'maxLength': 250},
                   },
    'required': ['wording']
}

channel_input_format = {
    'type': 'object',
    'properties': {'name': {'type': 'string', 'maxLength': 250},
                   'max_size': {'type': ['integer', 'null']},
                   'content_type': {'type': 'string', 'maxLength': 250}
    },
    'required': ['name', 'max_size', 'content_type']
}

message_input_format = {
    'type': 'object',
    'properties': {'text': {'type': 'string'},
                   'channel': {'type': 'object',
                               'properties': {
                                   'id': {
                                       'type': 'string', 'pattern': id_format_text
                                   }
                               },
                               'required': ['id']
                   }
    },
    'required': ['text', 'channel']
}

impact_input_format = {
    'type': 'object',
    'properties': {
        'severity': {'type': 'object',
                     'properties': {'id': {'type': 'string', 'pattern': id_format_text}},
                     'required': ['id']
        },
        'application_periods': {'type': 'array',
                                'items': [date_period_format]
        },
        'objects': {'type': 'array',
                    'items': [object_input_format]
        },
        'messages': {'type': 'array',
                     'items': [message_input_format]
        }
    },
    'required': ['severity']
}
