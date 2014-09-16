from nose.tools import *
from chaos.utils import is_pt_object_valid


class Obj(object):
    pass


def filter_constructor_object_type_valid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,'stop_area', None), True)


def filter_constructor_uri_valid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,None, 'b'), True)


def filter_constructor_object_type_invalid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,'network', None), True)


def filter_constructor_uri_invalid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,None, 'c'), False)


def filter_constructor_uris_valid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,None, ['c', 'b']), True)


def filter_constructor_uris_valid_pt_object_type_invalid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,'network', ['c', 'b']), True)


def filter_constructor_uri_invalid_pt_object_type_valid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,'stop_area', 'c'), False)


def filter_constructor_uris_valid_pt_object_type_valid():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,'stop_area', ['c', 'b']), True)


def filter_constructor_not_uri_and_not_pt_object_type():
    one_pt_object = Obj()
    one_pt_object.uri = 'b'
    one_pt_object.type = 'stop_area'
    eq_(is_pt_object_valid(one_pt_object,None, None), False)
