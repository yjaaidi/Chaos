from nose.tools import *
from flask import g
from aniso8601 import parse_datetime
from datetime import datetime
import chaos

#current_time exists
def test_current_time():
    with chaos.app.app_context():
        g.current_time = parse_datetime("2014-10-10T13:15:00Z").replace(tzinfo=None)
        eq_(chaos.utils.get_current_time(), g.current_time)


#current_time is exists in g and g.current_time None
def test_now_current_time1():
    with chaos.app.app_context():
        g.current_time = None
        eq_(datetime.utcnow() < chaos.utils.get_current_time(), True)


#current_time is not exists
def test_now_current_time2():
    with chaos.app.app_context():
        eq_(datetime.utcnow() < chaos.utils.get_current_time(), True)
