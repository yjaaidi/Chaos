from nose.tools import *
from chaos import fields, models
from datetime import datetime

class Obj(object):
    pass

def test_none_field_date_time():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format(None), 'null')

@raises(AttributeError)
def test_field_date_time_valid():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format('2014-08-07 12:46:56.837613'), 'null')

def test_field_date_time_valid():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format(datetime(2014, 2, 10,13, 5, 10)), '2014-02-10T13:05:10Z')

def test_name_channel():
    channel = models.Channel()
    eq_(str(channel), "<Channel '{}'>".format(channel.id))

def test_name_impact():
    impact = models.Impact()
    eq_(str(impact), "<Impact '{}'>".format(impact.id))

def test_name_disruption():
    disruption = models.Disruption()
    eq_(str(disruption), "<Disruption '{}'>".format(disruption.id))