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
    def all(cls, publication_status):
        to_return = cls.query.filter_by(status='published')
        publication_status = set(publication_status)

        if len(publication_status) == len(publication_status_values):
            return to_return
        elif len(publication_status) == 1:
            #past
            # Filter all disruption with end_publication_date < now.
            if 'past' in publication_status:
                to_return = to_return.filter(cls.end_publication_date < get_current_time())
            #ongoing
            # Filter all disruption with start_publication_date <= now <= end_publication_date.
            if 'ongoing' in publication_status:
                to_return = to_return.filter(cls.start_publication_date <= get_current_time()).filter(cls.end_publication_date >= get_current_time())
            #coming
            # Filter all disruption with start_publication_date > now.
            elif 'coming' in publication_status:
                to_return = to_return.filter(cls.start_publication_date > get_current_time())
        elif len(publication_status) == 2:
            #past and ongoing
            #Filter with (end_publication_date < now) or (start_publication_date < now and end_publication_date > now)
            if 'past' in publication_status and 'ongoing' in publication_status:
                to_return = to_return.filter(or_(cls.end_publication_date < get_current_time(),
                                                 and_(cls.start_publication_date < get_current_time(),
                                                      cls.end_publication_date > get_current_time())))
            # ongoing and coming
            #Filter with  (start_publication_date > now) (start_publication_date < now and end_publication_date > now)
            elif 'ongoing' in publication_status and 'coming' in publication_status:
                to_return = to_return.filter(or_(cls.start_publication_date > get_current_time(),
                                                 and_(cls.start_publication_date < get_current_time(),
                                                      cls.end_publication_date > get_current_time())))
            # past and coming
            #Filter with  (end_publication_date < now) or (start_publication_date > now)
            elif 'past' in publication_status and 'coming' in publication_status:
                to_return = to_return.filter(or_(cls.end_publication_date < get_current_time(),cls.start_publication_date > get_current_time()))

        return to_return

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

