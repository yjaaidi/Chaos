from nose.tools import *
from chaos.navitia import Navitia, exceptions
import json
import requests

from httmock import all_requests, HTTMock, response


class NavitiaMock(object):
    def __init__(self, response_code, json, assert_url=None):
        self.response_code = response_code
        self.json = json
        self.assert_url = assert_url

    @all_requests
    def __call__(self, url, request):
        if self.assert_url:
            eq_(self.assert_url, request.url)
        return response(self.response_code, json.dumps(self.json))


@all_requests
def navitia_mock_navitia_error(url, request):
    raise exceptions.NavitiaError

@all_requests
def navitia_mock_unknown_object_type(url, request):
    raise exceptions.ObjectTypeUnknown

def test_get_pt_object():
    n = Navitia('http://api.navitia.io', 'jdr')
    mock = NavitiaMock(200, {'networks': [{'id': 'network:foo', 'name': 'reseau foo'}]},
            assert_url='http://api.navitia.io/v1/coverage/jdr/networks/network:foo?depth=0')
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), {'id': 'network:foo', 'name': 'reseau foo'})

    mock = NavitiaMock(200, {'networks': []})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), None)

    mock = NavitiaMock(404, {})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), None)


@raises(exceptions.NavitiaError)
def test_navitia_request_error():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_navitia_error):
        n.get_pt_object('network:foo','network')

@raises(exceptions.ObjectTypeUnknown)
def test_navitia_unknown_object_type():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_unknown_object_type):
        n.get_pt_object('network:foo', 'aaaaaaaa')


def test_query_formater():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri?depth=0')


def test_query_formater_line_section():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'line_section'), None)


def test_query_formater_all():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network', 'networks'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri/networks?depth=0')

@raises(exceptions.ObjectTypeUnknown)
def test_query_formater_all_objects_invalid():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network', 'stop_areas'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri/networks?depth=0')
