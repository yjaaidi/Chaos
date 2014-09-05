from nose.tools import *
from flask import g
from aniso8601 import parse_datetime
from datetime import datetime
import chaos

#current_time exists
def test_get_date_time_valid():
    with chaos.app.app_context():
        str_date_time = "2014-10-10T13:15:00Z"
        date_time = parse_datetime(str_date_time).replace(tzinfo=None)
        eq_(chaos.utils.get_datetime(str_date_time, 'strtodatetime'), date_time)

@raises(ValueError)
def test_get_date_time_invalid():
    with chaos.app.app_context():
        str_date_time = "2014-02-30T13:15:00Z"
        date_time = parse_datetime(str_date_time).replace(tzinfo=None)
        eq_(chaos.utils.get_datetime(str_date_time, 'strtodatetime'), date_time)