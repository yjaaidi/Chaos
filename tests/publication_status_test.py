from nose.tools import *
from datetime import datetime, timedelta
import chaos


def test_publication_status_past():
    with chaos.app.app_context():
        ob = chaos.models.Disruption()
        now = datetime.utcnow()
        ob.start_publication_date = now + timedelta(days=-4)
        ob.end_publication_date = now + timedelta(days=-1)
        eq_(ob.publication_status,  'past')


def test_publication_status_ongoing():
    with chaos.app.app_context():
        ob = chaos.models.Disruption()
        ob.start_publication_date = datetime.utcnow()
        ob.end_publication_date = ob.start_publication_date + timedelta(days=2)
        eq_(ob.publication_status,  'ongoing')


def test_publication_status_coming():
    with chaos.app.app_context():
        ob = chaos.models.Disruption()
        ob.start_publication_date = datetime.utcnow() + timedelta(days=1)
        ob.end_publication_date = ob.start_publication_date + timedelta(days=3)
        eq_(ob.publication_status,  'coming')

def test_publication_status_coming_not_end_publication_date():
    with chaos.app.app_context():
        ob = chaos.models.Disruption()
        ob.start_publication_date = datetime.utcnow() + timedelta(days=1)
        ob.end_publication_date = None
        eq_(ob.publication_status,  'coming')

def test_publication_status_ongoing_not_end_publication_date():
    with chaos.app.app_context():
        ob = chaos.models.Disruption()
        ob.start_publication_date = datetime.utcnow() + timedelta(days=-1)
        ob.end_publication_date = None
        eq_(ob.publication_status,  'ongoing')
