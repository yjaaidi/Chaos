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
from sqlalchemy import or_, and_

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



class Disruption(TimestampMixin, db.Model):
    id = db.Column(UUID, primary_key=True)
    reference = db.Column(db.Text, unique=False, nullable=True)
    note = db.Column(db.Text, unique=False, nullable=True)
    status = db.Column(DisruptionStatus, nullable=False, default='published', index=True)
    start_publication_date = db.Column(db.DateTime(), nullable=True)
    end_publication_date = db.Column(db.DateTime(), nullable=True)

    def __repr__(self):
        return '<Disruption %r>' % self.id

    def __init__(self):
        self.id = str(uuid.uuid1())

    def archive(self):
        """
        archive the disruption, it will not be visible on any media
        """
        self.status = 'archived'

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id, status='published').first_or_404()

    @classmethod
    @paginate()
    def all_with_filter(cls, publication_status):
        availlable_filters = {'past': and_(cls.end_publication_date != None, cls.end_publication_date < get_current_time()),
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
        if self.end_publication_date < current_time:
            return "past"
        # ongoing
        if self.start_publication_date <= current_time <= self.end_publication_date:
            return "ongoing"
        # Coming
        if self.start_publication_date > current_time:
            return "coming"

