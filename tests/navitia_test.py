from nose.tools import *
from chaos.navitia import Navitia, exceptions
import json
import requests
from retrying import retry


from httmock import all_requests, HTTMock, response


class NavitiaMock(object):
    def __init__(self, response_code, json, assert_url=None):
        self.response_code = response_code
        self.json = json
        self.assert_url = assert_url

    @all_requests
    def __call__(self, url, request):
        # Temporary fix for tests to pass (due to first request for publication date)
        if request.url == 'http://api.navitia.io/v1/coverage/jdr/status':
            return response(200, json.dumps({'status': {'publication_date': '20170309T143733.933792'}}))

        if self.assert_url:
            eq_(self.assert_url, request.url)
        return response(self.response_code, json.dumps(self.json))


@all_requests
def navitia_mock_navitia_error(url, request):
    raise exceptions.NavitiaError

@all_requests
def navitia_mock_navitia_unauthorized(url, request):
    return response(401, json.dumps({'message': 'test unauthorized'}))


@all_requests
def navitia_mock_unknown_object_type(url, request):
    # Temporary fix for tests to pass (due to first request for publication date)
    if request.url == 'http://api.navitia.io/v1/coverage/jdr/status':
        return response(200, json.dumps({'status': {'publication_date': '20170309T143733.933792'}}))
    raise exceptions.ObjectTypeUnknown


def test_get_pt_object():
    n = Navitia('http://api.navitia.io', 'jdr')
    mock = NavitiaMock(200, {'networks': [{'id': 'network:foo', 'name': 'reseau foo'}]},
                       assert_url='http://api.navitia.io/v1/coverage/jdr/networks/network:foo?depth=0&disable_disruption=true')
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), {'id': 'network:foo', 'name': 'reseau foo'})

    mock = NavitiaMock(200, {'networks': []})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo1', 'network'), None)

    mock = NavitiaMock(404, {})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo2', 'network'), None)


@raises(exceptions.NavitiaError)
def test_navitia_request_error():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_navitia_error):
        n.get_pt_object('network:foo3','network')


@raises(exceptions.ObjectTypeUnknown)
def test_navitia_unknown_object_type():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_unknown_object_type):
        n.get_pt_object('network:foo4', 'aaaaaaaa')


def test_query_formater():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri?depth=0&disable_disruption=true')


def test_query_formater_line_section():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'line_section'), None)


def test_query_formater_all():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network', 'networks'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri/networks?depth=0&disable_disruption=true')


@raises(exceptions.ObjectTypeUnknown)
def test_query_formater_all_objects_invalid():
    n = Navitia('http://api.navitia.io', 'jdr')
    eq_(n.query_formater('uri', 'network', 'stop_areas'), 'http://api.navitia.io/v1/coverage/jdr/networks/uri/networks?depth=0&disable_disruption=true')


navitia_timeout_count = 0
@raises(requests.exceptions.Timeout)
def test_navitia_retry():
    n = Navitia('http://api.navitia.io', 'jdr')

    def navitia_timeout_response(*args, **kwargs):
        global navitia_timeout_count
        navitia_timeout_count += 1
        raise requests.exceptions.Timeout
    requests.get = navitia_timeout_response
    n._navitia_caller('http://api.navitia.io')
    eq_(navitia_timeout_count, 3)

@raises(exceptions.Unauthorized)
def test_navitia_unauthorized():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_navitia_unauthorized):
        try:
            n._navitia_caller('http://api.navitia.io')
        except exceptions.Unauthorized as e:
            eq_(e.message, 'test unauthorized')
            raise
