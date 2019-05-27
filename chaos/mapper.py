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

from collections import Mapping, Sequence
from aniso8601 import parse_datetime, parse_time, parse_date
from chaos import models

class Datetime(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __call__(self, item, field, value):
        if value:
            setattr(
                item,
                self.attribute,
                parse_datetime(value).replace(tzinfo=None)
            )
        else:
            setattr(item, self.attribute, None)


class Time(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __call__(self, item, field, value):
        if value:
            setattr(
                item,
                self.attribute,
                parse_time(value).replace(tzinfo=None)
            )
        else:
            setattr(item, self.attribute, None)


class Date(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __call__(self, item, field, value):
        if value:
            setattr(item, self.attribute, parse_date(value))
        else:
            setattr(item, self.attribute, None)


class AliasText(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __call__(self, item, field, value):
        setattr(item, self.attribute, value)


class OptionalField(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __call__(self, item, field, json):
        if field in json and json[field] is not None:
            setattr(item, self.attribute, json[field])


def fill_from_json(item, json, fields):
    for field, formater in fields.iteritems():
        if isinstance(formater, OptionalField):
            formater(item, field, json)
        else:
            if field not in json:
                setattr(item, field, None)
                continue
            if isinstance(formater, Mapping):
                fill_from_json(item, json[field], fields=formater)
            elif isinstance(formater, Sequence):
                for fr in formater:
                    for key in fr.keys():
                        for one_json in json[field]:
                            fr[key](item, key, one_json[key])
            elif not formater:
                setattr(item, field, json[field])
            elif formater:
                formater(item, field, json[field])


disruption_mapping = {
    'reference': None,
    'note': None,
    'status': OptionalField(attribute='status'),
    'publication_period': {
        'begin': Datetime(attribute='start_publication_date'),
        'end': Datetime(attribute='end_publication_date')
    },
    'cause': {'id': AliasText(attribute='cause_id')}
}

severity_mapping = {
    'color': None,
    'priority': None,
    'effect': None,
}

cause_mapping = {
    'category': {'id': AliasText(attribute='category_id')},
}

tag_mapping = {
    'name': None
}

property_mapping = {
    'key': None,
    'type': None
}

category_mapping = {
    'name': None
}

object_mapping = {
    "id": AliasText(attribute='uri'),
    "type": None
}

message_mapping = {
    "text": None,
    'channel': {'id': AliasText(attribute='channel_id')}
}

meta_mapping = {
    'key': None,
    'value': None
}

application_period_mapping = {
    'begin': Datetime(attribute='start_date'),
    'end': Datetime(attribute='end_date')
}

channel_mapping = {
    'name': None,
    'max_size': None,
    'content_type': None,
    'required': OptionalField(attribute='required')
}

line_section_mapping = {
    'line': None,
    'start_point': None,
    'end_point': None,
    'sens': None
}

pattern_mapping = {
    'start_date': Date(attribute='start_date'),
    'end_date': Date(attribute='end_date'),
    'weekly_pattern': None,
    'time_zone': None
}

time_slot_mapping = {
    'begin': Time(attribute='begin'),
    'end': Time(attribute='end')
}

export_mapping = {
    'start_date': Datetime(attribute='start_date'),
    'end_date': Datetime(attribute='end_date'),
    'time_zone': None
}

def get_datetime_from_json_attr(json, attr):
    return parse_datetime(json[attr]).replace(tzinfo=None) if attr in json and json[attr] else None


def disruption_from_history(disruption, json):
    contributor = models.Contributor()
    contributor.contributor_code = json['contributor']

    cause_wordings = []

    for wording in json['cause']['wordings']:
        wording_model = models.Wording()
        wording_model.key = wording['key']
        wording_model.value = wording['value']
        cause_wordings.append(wording_model)

    cause = models.Cause()
    cause.id = json['cause']['id']
    cause.created_at = get_datetime_from_json_attr(json['cause'], 'created_at')
    cause.updated_at = get_datetime_from_json_attr(json['cause'], 'updated_at')
    cause.wordings = cause_wordings

    if json['cause']['category']:
        cause.category = models.Category()
        cause.category.id = json['cause']['category']['id']
        cause.category.created_at = get_datetime_from_json_attr(json['cause']['category'], 'created_at')
        cause.category.updated_at = get_datetime_from_json_attr(json['cause']['category'], 'updated_at')
        cause.category.name = json['cause']['category']['name']

    disruption_tags = []
    for tag in json['tags']:
        tag_model = models.Tag()
        tag_model.id = tag['id']
        tag_model.created_at = get_datetime_from_json_attr(tag, 'created_at')
        tag_model.updated_at = get_datetime_from_json_attr(tag, 'updated_at')
        tag_model.name = tag['name']
        disruption_tags.append(tag_model)

    disruption_properties = []
    for property in json['properties']:
        property_model = models.Property()
        property_model.id = property['id']
        disruption_properties.append(property_model)

    disruption.id = json['id']
    disruption.reference = json['reference']
    disruption.note = json['note']
    disruption.status = json['status']
    disruption.version = json['version']
    disruption.created_at = get_datetime_from_json_attr(json, 'created_at')
    disruption.updated_at = get_datetime_from_json_attr(json, 'updated_at')
    disruption.reference = json['reference']
    disruption.start_publication_date = get_datetime_from_json_attr(json['publication_period'], 'begin')
    disruption.end_publication_date = get_datetime_from_json_attr(json['publication_period'], 'end')
    disruption.publicationStatus = json['publication_status']
    disruption.contributor = contributor
    disruption.cause = cause
    disruption.tags = disruption_tags
    disruption.properties = disruption_properties
    disruption.history_localization = json['localization']
