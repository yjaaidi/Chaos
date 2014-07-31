# encoding: utf-8

#  Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
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

import uuid
from chaos import db, utils
from utils import paginate, get_current_time
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from formats import publication_status_values
from sqlalchemy import or_, and_, not_
from sqlalchemy.orm import aliased


#force the server to use UTC time for each connection
import sqlalchemy


def set_utc_on_connect(dbapi_con, con_record):
    c = dbapi_con.cursor()
    c.execute("SET timezone='utc'")
    c.close()
sqlalchemy.event.listen(sqlalchemy.pool.Pool, 'connect', set_utc_on_connect)


class TimestampMixin(object):
    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime(), default=None, onupdate=datetime.utcnow)

DisruptionStatus = db.Enum('published', 'archived', name='disruption_status')
SeverityEffect = db.Enum('blocking', name='severity_effect')
ImpactStatus = db.Enum('published', 'archived', name='impact_status')
PtObjectType = db.Enum('network', 'stop_area', 'line', name='pt_object_type')


class Severity(TimestampMixin, db.Model):
    """
    represent the severity of an impact
    """
    id = db.Column(UUID, primary_key=True)
    wording = db.Column(db.Text, unique=False, nullable=False)
    color = db.Column(db.Text, unique=False, nullable=True)
    is_visible = db.Column(db.Boolean, unique=False, nullable=False, default=True)
    priority = db.Column(db.Integer, unique=False, nullable=True)
    effect = db.Column(SeverityEffect, nullable=True)

    def __init__(self):
        self.id = str(uuid.uuid1())

    def __repr__(self):
        return '<Severity %r>' % self.id

    @classmethod
    def all(cls):
        return cls.query.filter_by(is_visible=True).order_by(cls.priority).all()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, is_visible=True).first_or_404()


class Cause(TimestampMixin, db.Model):
    """
    represent the cause of a disruption
    """
    id = db.Column(UUID, primary_key=True)
    wording = db.Column(db.Text, unique=False, nullable=False)
    is_visible = db.Column(db.Boolean, unique=False, nullable=False, default=True)

    def __init__(self):
        self.id = str(uuid.uuid1())

    def __repr__(self):
        return '<Cause %r>' % self.id

    @classmethod
    def all(cls):
        return cls.query.filter_by(is_visible=True).all()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, is_visible=True).first_or_404()


class Tag(TimestampMixin, db.Model):
    """
    represent the tag of a disruption
    """
    __tablename__ = 'tag'
    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    is_visible = db.Column(db.Boolean, unique=False, nullable=False, default=True)

    disruptions = db.relationship("Disruption", secondary='associate_disruption_tag')

    def __init__(self):
        self.id = str(uuid.uuid1())

    def __repr__(self):
        return '<Tag %r>' % self.id

    @classmethod
    def all(cls):
        return cls.query.filter_by(is_visible=True).all()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, is_visible=True).first_or_404()


class Disruption(TimestampMixin, db.Model):
    __tablename__ = 'disruption'
    id = db.Column(UUID, primary_key=True)
    reference = db.Column(db.Text, unique=False, nullable=True)
    note = db.Column(db.Text, unique=False, nullable=True)
    status = db.Column(DisruptionStatus, nullable=False, default='published', index=True)
    start_publication_date = db.Column(db.DateTime(), nullable=True)
    end_publication_date = db.Column(db.DateTime(), nullable=True)
    impacts = db.relationship('Impact', backref='disruption', lazy='dynamic')
    localization_id = db.Column(db.Text, unique=False, nullable=True)
    cause_id = db.Column(UUID, db.ForeignKey(Cause.id))
    cause = db.relationship('Cause', backref='disruption', lazy='joined')
    tags = db.relationship("Tag", secondary='associate_disruption_tag', lazy='joined')

    def __repr__(self):
        return '<Disruption %r>' % self.id

    def __init__(self):
        self.id = str(uuid.uuid1())

    def archive(self):
        """
        archive the disruption, it will not be visible on any media
        """
        self.status = 'archived'
        for impact in self.impacts:
            impact.archive()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, status='published').first_or_404()

    @classmethod
    @paginate()
    def all_with_filter(cls, publication_status):
        availlable_filters = {
            'past': and_(cls.end_publication_date != None, cls.end_publication_date < get_current_time()),
            'ongoing': and_(cls.start_publication_date <= get_current_time(),
                            or_(cls.end_publication_date == None, cls.end_publication_date >= get_current_time())),
            'coming': Disruption.start_publication_date > get_current_time()
        }
        query = cls.query.filter_by(status='published')
        publication_status = set(publication_status)
        if len(publication_status) == len(publication_status_values):
            return query
        else:
            filters = [availlable_filters[status] for status in publication_status]
            query = query.filter(or_(*filters))
            return query

    @property
    def publication_status(self):


        current_time = utils.get_current_time()
        # Past
        if (self.end_publication_date != None) and (self.end_publication_date < current_time):
            return "past"
        # ongoing
        if self.start_publication_date <= current_time\
            and (self.end_publication_date == None or self.end_publication_date >= current_time):
            return "ongoing"
        # Coming
        if self.start_publication_date > current_time:
            return "coming"

class AssociateDisruptionTag(TimestampMixin, db.Model):
    """
    represents the associate disruption and tag
    """
    __tablename__ = 'associate_disruption_tag'
    id = db.Column(UUID, primary_key=True)
    disruption_id = db.Column(UUID, db.ForeignKey('disruption.id'), index=True)
    tag_id = db.Column(UUID, db.ForeignKey('tag.id'), index=True)

    def __init__(self, disruption_id=None, tag_id=None):
        self.id = str(uuid.uuid1())
        self.disruption_id = disruption_id
        self.tag_id = tag_id

    def __repr__(self):
        return '<AsociateDisruptionTag %r>' % self.id

    @classmethod
    def get(cls, disruption_id, tag_id):
        return cls.query.filter_by(disruption_id=disruption_id, tag_id=tag_id).first_or_404()

class Impact(TimestampMixin, db.Model):
    id = db.Column(UUID, primary_key=True)
    status = db.Column(ImpactStatus, nullable=False, default='published', index=True)
    disruption_id = db.Column(UUID, db.ForeignKey(Disruption.id))
    severity_id = db.Column(UUID, db.ForeignKey(Severity.id))
    objects = db.relationship('PTobject', backref='impact', lazy='joined')
    messages = db.relationship('Message', backref='impact', lazy='joined')
    application_periods = db.relationship('ApplicationPeriods', backref='impact', lazy='joined')
    severity = db.relationship('Severity', backref='impacts', lazy='joined')

    def __repr__(self):
        return '<Impact %r>' % self.id

    def __marshallable__(self):
        '''
        This method is added to solve the problem of impact without instance during creation of response json for Post..
        API post cannot fill url for impact and disruption in impact_fields
        When we have either one of them present in impact_fields, it works.
        '''
        d = {}
        d['id'] = self.id
        d['status'] = self.status
        d['disruption_id'] = self.disruption_id
        d['severity_id'] = self.severity_id
        d['objects'] = self.objects
        d['application_periods'] = self.application_periods
        d['severity'] = self.severity
        d['messages'] = self.messages
        return d

    def __init__(self, objects=None):
        self.id = str(uuid.uuid1())
        if objects:
            self.objects = objects

    def archive(self):
        """
        archive the impact, it will not be visible on any media
        """
        self.status = 'archived'

    def insert_object(self, object):
        """
        Adds an objectTC in a imapct.
        """
        self.objects.append(object)
        db.session.add(object)

    def insert_message(self, message):
        """
        Adds an message in a imapct.
        """
        self.messages.append(message)
        db.session.add(message)

    def delete_message(self, message):
        """
        delete an message in a imapct.
        """
        self.messages.remove(message)
        db.session.delete(message)

    def insert_app_period(self, application_period):
        """
        Adds an objectTC in a imapct.
        """
        self.application_periods.append(application_period)
        db.session.add(application_period)

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, status='published').first_or_404()

    @classmethod
    @paginate()
    def all(cls, disruption_id):
        alias = aliased(Severity)
        query = cls.query.filter_by(status='published')
        query = query.filter(and_(cls.disruption_id == disruption_id))
        return query.join(alias, Impact.severity).order_by(alias.priority)

    @classmethod
    def all_with_filter(cls, start_date, end_date, pt_object_type, uris):
        query = cls.query.filter_by(status='published')
        query = query.join(PTobject)

        if pt_object_type:
            query = query.filter(and_(PTobject.type == pt_object_type))

        query = query.join(ApplicationPeriods)
        query = query.filter(
            and_(
                or_(
                    not_(
                        or_(
                            ApplicationPeriods.start_date > end_date,
                            ApplicationPeriods.end_date < start_date
                        )
                    ),
                    and_(
                        ApplicationPeriods.start_date <= end_date,
                        ApplicationPeriods.end_date == None
                    )
                )
            )
        )

        if uris:
            query = query.filter(PTobject.uri.in_(uris))

        query = query.order_by(ApplicationPeriods.start_date)
        return query.all()


class PTobject(TimestampMixin, db.Model):
    __tablename__ = 'pt_object'
    id = db.Column(UUID, primary_key=True)
    type = db.Column(PtObjectType, nullable=False, default='network', index=True)
    uri = db.Column(db.Text, primary_key=True)
    impact_id = db.Column(UUID, db.ForeignKey(Impact.id), index=True)

    def __repr__(self):
        return '<PTobject %r>' % self.id

    def __init__(self, impact_id=None, type=None, code=None):
        self.id = str(uuid.uuid1())
        self.impact_id = impact_id
        self.type = type
        self.uri = code

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first_or_404()


class ApplicationPeriods(TimestampMixin, db.Model):
    """
    represents the application periods of an impact
    """
    id = db.Column(UUID, primary_key=True)
    start_date = db.Column(db.DateTime(), nullable=True)
    end_date = db.Column(db.DateTime(), nullable=True)
    impact_id = db.Column(UUID, db.ForeignKey(Impact.id), index=True)

    def __init__(self, impact_id=None):
        self.id = str(uuid.uuid1())
        self.impact_id = impact_id

    def __repr__(self):
        return '<ApplicationPeriods %r>' % self.id


class Channel(TimestampMixin, db.Model):
    """
    represent the channel for the message of an impact
    """
    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    max_size = db.Column(db.Integer, unique=False, nullable=True)
    content_type = db.Column(db.Text, unique=False, nullable=True)
    is_visible = db.Column(db.Boolean, unique=False, nullable=False, default=True)

    def __init__(self):
        self.id = str(uuid.uuid1())

    def __repr__(self):
        return '<Channel %r>' % self.id

    @classmethod
    def all(cls):
        return cls.query.filter_by(is_visible=True).all()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, is_visible=True).first_or_404()


class Message(TimestampMixin, db.Model):
    """
    represent the message of an impact
    """
    id = db.Column(UUID, primary_key=True)
    text = db.Column(db.Text, unique=False, nullable=False)
    impact_id = db.Column(UUID, db.ForeignKey(Impact.id))
    channel_id = db.Column(UUID, db.ForeignKey(Channel.id))
    channel = db.relationship('Channel', backref='message', lazy='select')

    def __init__(self):
        self.id = str(uuid.uuid1())

    def __repr__(self):
        return '<Message %r>' % self.id

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first_or_404()
