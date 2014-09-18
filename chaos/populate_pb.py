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

import chaos_pb2, gtfs_realtime_pb2
import time


def get_pos_time(sql_time):
    if sql_time:
        return int(time.mktime(sql_time.timetuple()))
    return 0


def get_pt_object_type(type):
    collection = {
        "network": chaos_pb2.PtObject.network,
        "stop_area": chaos_pb2.PtObject.stop_area,
        "line": chaos_pb2.PtObject.line,
        "line_section": chaos_pb2.PtObject.line_section,
        "route": chaos_pb2.PtObject.route
    }
    if type in collection:
        return collection[type]
    return chaos_pb2.PtObject.unkown_type


def created_upated_at(src, dest):
    dest.created_at = get_pos_time(src.created_at)
    if src.updated_at:
        dest.updated_at = get_pos_time(src.updated_at)


def populate_severity(impact_pb, severity):
    impact_pb.severity.id = severity.id
    impact_pb.severity.wording = severity.wording
    if severity.color:
        impact_pb.severity.color = severity.color
    if severity.effect:
        impact_pb.severity.effect = gtfs_realtime_pb2.Alert.NO_SERVICE
    else:
        impact_pb.severity.effect = gtfs_realtime_pb2.Alert.UNKNOWN_EFFECT


def populate_application_periods(impact, impact_pb):
    for application_period in impact.application_periods:
        application_period_pb = impact_pb.application_periods.add()
        application_period_pb.start = get_pos_time(application_period.start_date)
        if application_period.end_date:
            application_period_pb.end = get_pos_time(application_period.end_date)


def populate_channel(channel_pb, channel):
    channel_pb.id = channel.id
    channel_pb.name = channel.name
    channel_pb.content_type = channel.content_type
    channel_pb.max_size = long(channel.max_size)
    created_upated_at(channel, channel_pb)


def populate_messages(impact, impact_pb):
    for message in impact.messages:
        message_pb = impact_pb.messages.add()
        message_pb.text = message.text
        created_upated_at(message, message_pb)
        populate_channel(message_pb.channel, message.channel)


def populate_pt_objects(impact, impact_pb):
    for pt_object in impact.objects:
        if pt_object.type != 'line_section':
            informed_entitie = impact_pb.informed_entities.add()
            informed_entitie.pt_object_type = get_pt_object_type(pt_object.type)
            informed_entitie.uri = pt_object.uri
            created_upated_at(pt_object, informed_entitie)


def populate_impact(disruption, disruption_pb):
    for impact in disruption.impacts:
        if impact.status == "published":
            impact_pb = disruption_pb.impacts.add()
            impact_pb.id = impact.id
            created_upated_at(impact, impact_pb)
            populate_severity(impact_pb, impact.severity)
            populate_application_periods(impact, impact_pb)
            populate_messages(impact, impact_pb)
            populate_pt_objects(impact, impact_pb)


def populate_localization(disruption, disruption_pb):
    localization_pb = disruption_pb.localization.add()
    localization_pb.stop_id = str(disruption.localization_id)


def populate_tag(disruption, disruption_pb):
    if disruption.tags:
        for tag in disruption.tags:
            tag_pb = disruption_pb.tags.add()
            tag_pb.id = tag.id
            tag_pb.name = tag.name
            created_upated_at(tag, tag_pb)


def populate_cause(cause, cause_pb):
    cause_pb.id = cause.id
    cause_pb.wording = cause.wording


def populate_disruption(disruption, disruption_pb):
    disruption_pb.id = disruption.id
    disruption_pb.reference = disruption.reference
    if disruption.note:
        disruption_pb.note = disruption.note
    created_upated_at(disruption, disruption_pb)
    disruption_pb.publication_periods.start = get_pos_time(disruption.start_publication_date)
    if disruption.end_publication_date:
        disruption_pb.publication_periods.end = get_pos_time(disruption.end_publication_date)
    if disruption.cause:
        populate_cause(disruption.cause, disruption_pb.cause)
    populate_localization(disruption, disruption_pb)
    populate_tag(disruption, disruption_pb)
    populate_impact(disruption, disruption_pb)


def populate_pb(disruption):
    feed_entity = gtfs_realtime_pb2.FeedEntity()
    feed_entity.id = disruption.id
    feed_entity.is_deleted = disruption.status == "archived"

    if not feed_entity.is_deleted:
        disruption_pb = feed_entity.Extensions[chaos_pb2.disruption]
        populate_disruption(disruption, disruption_pb)
    return feed_entity
