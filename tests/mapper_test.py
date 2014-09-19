from nose.tools import *

from chaos import mapper
from datetime import datetime

class Obj(object):
    pass

def test_datetime():
    m = mapper.Datetime('foo')
    obj = Obj()
    obj.foo = None
    m(obj,  'foo', '2014-06-02T22:03:01')
    eq_(obj.foo, datetime(2014, 6, 2, 22, 3, 1))

@raises(ValueError)
def test_datetime_invalid():
    m = mapper.Datetime('foo')
    obj = Obj()
    obj.foo = None
    m(obj,  'foo', '2014-06-02T:03:01')

def test_fill_from_json():
    obj = Obj()
    obj.foo = None
    obj.baz = None
    json = {'foo': 'bar', 'baz': 2}
    fields = {'foo': None, 'baz': None}

    mapper.fill_from_json(obj, json, fields)
    eq_(obj.foo, 'bar')
    eq_(obj.baz, 2)

def test_fill_from_json_with_nested():
    obj = Obj()
    obj.foo = None
    obj.bar = None
    json = {'foo': 'bar', 'baz': {'bar': 2}}
    fields = {'foo': None, 'baz': {'bar': None}}

    mapper.fill_from_json(obj, json, fields)
    eq_(obj.foo, 'bar')
    eq_(obj.bar, 2)


def test_fill_from_json_with_formater():
    obj = Obj()
    obj.date = None
    fields = {'date': mapper.Datetime('date')}
    json = {'date': '2014-05-22T12:15:23'}

    mapper.fill_from_json(obj, json, fields)
    eq_(obj.date, datetime(2014, 5, 22, 12, 15, 23))

def test_fill_from_json_with_missing_json():
    obj = Obj()
    obj.foo = 1
    fields = {'foo': None}
    json = {'bar': 3}

    mapper.fill_from_json(obj, json, fields)
    eq_(obj.foo, None)


def test_alias_text_value_valid():
    obj = Obj()
    obj.value = 'AA'
    text_alis = mapper.AliasText('value')
    text_alis(obj, 'field', 'bb')
    eq_(obj.value, 'bb')

def test_alias_text_value_not_valid():
    obj = Obj()
    obj.value = 'AA'
    text_alis = mapper.AliasText('value')
    text_alis(obj, 'field', None)
    eq_(obj.value, None)
