from nose.tools import *
from chaos import fields
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
