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


class PopulatePb(object):
    def __init__(self, disruption, is_deleted=False):
        self.disruption = disruption
        self.feed_entity = gtfs_realtime_pb2.FeedEntity()
        self.extend_feed_entity = self.feed_entity.Extensions[chaos_pb2.disruption]
        self.feed_entity.is_deleted = is_deleted
        self.feed_entity.id = disruption.id

    def get_pt_object_type(self, type):
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

    def created_upated_at(self, src, dest):
        dest.created_at = get_pos_time(src.created_at)
        if src.updated_at:
            dest.updated_at = get_pos_time(src.updated_at)

    def populate_severity(self, impact_pb, severity):
        impact_pb.severity.id = severity.id
        impact_pb.severity.wording = severity.wording
        if severity.color:
            impact_pb.severity.color = severity.color
        if severity.effect:
            impact_pb.severity.effect = gtfs_realtime_pb2.Alert.NO_SERVICE
        else:
            impact_pb.severity.effect = gtfs_realtime_pb2.Alert.UNKNOWN_EFFECT

    def populate_application_periods(self, impact, impact_pb):
        for application_period in impact.application_periods:
            application_period_pb = impact_pb.application_periods.add()
            application_period_pb.start = get_pos_time(application_period.start_date)
            if application_period.end_date:
                application_period_pb.end = get_pos_time(application_period.end_date)

    def populate_channel(self, channel_pb, channel):
        channel_pb.id = channel.id
        channel_pb.name = channel.name
        channel_pb.content_type = channel.content_type
        channel_pb.max_size = long(channel.max_size)
        self.created_upated_at(channel, channel_pb)

    def populate_messages(self, impact, impact_pb):
        for message in impact.messages:
            message_pb = impact_pb.messages.add()
            message_pb.text = message.text
            self.created_upated_at(message, message_pb)
            self.populate_channel(message_pb.channel, message.channel)

    def populate_pt_objects(self, impact, impact_pb):
        for pt_object in impact.objects:
            if pt_object.type != 'line_section':
                informed_entitie = impact_pb.informed_entities.add()
                informed_entitie.pt_object_type = self.get_pt_object_type(pt_object.type)
                informed_entitie.uri = pt_object.uri
                self.created_upated_at(pt_object, informed_entitie)

    def populate_impact(self):
        for impact in self.disruption.impacts:
            impact_pb = self.extend_feed_entity.impacts.add()
            impact_pb.id = impact.id
            self.created_upated_at(impact, impact_pb)
            self.populate_severity(impact_pb, impact.severity)
            self.populate_application_periods(impact, impact_pb)
            self.populate_messages(impact, impact_pb)
            self.populate_pt_objects(impact, impact_pb)

    def populate_localization(self):
        localization = self.extend_feed_entity.localization.add()
        localization.stop_id = str(self.disruption.localization_id)

    def populate_tag(self):
        if self.disruption.tags:
            for tag in self.disruption.tags:
                tag_pb = self.extend_feed_entity.tags.add()
                tag_pb.id = tag.id
                tag_pb.name = tag.name
                self.created_upated_at(tag, tag_pb)

    def populate_cause(self):
        self.extend_feed_entity.cause.id = self.disruption.cause.id
        self.extend_feed_entity.cause.wording = self.disruption.cause.wording

    def populate_disruption(self):
        self.extend_feed_entity.id = self.disruption.id
        self.extend_feed_entity.reference = self.disruption.reference
        if self.disruption.note:
            self.extend_feed_entity.note = self.disruption.note
        self.created_upated_at(self.disruption, self.extend_feed_entity)
        self.extend_feed_entity.publication_periods.start = get_pos_time(self.disruption.start_publication_date)
        if self.disruption.end_publication_date:
            self.extend_feed_entity.publication_periods.end = get_pos_time(self.disruption.end_publication_date)
        self.populate_cause()
        self.populate_localization()
        self.populate_tag()
        self.populate_impact()

    def populate(self):
        if self.feed_entity.is_deleted:
            return
        self.populate_disruption()
