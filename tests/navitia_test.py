from nose.tools import *
from chaos.navitia import Navitia
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
def navitia_mock_timeout(url, request):
    raise requests.exceptions.Timeout()

def test_get_pt_object():
    n = Navitia('http://api.navitia.io', 'jdr')
    mock = NavitiaMock(200, {'networks': [{'id': 'network:foo', 'name': 'reseau foo'}]},
            assert_url='http://api.navitia.io/v1/coverage/jdr/networks/network:foo')
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), {'id': 'network:foo', 'name': 'reseau foo'})

    mock = NavitiaMock(200, {'networks': []})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), None)

    mock = NavitiaMock(404, {})
    with HTTMock(mock):
        eq_(n.get_pt_object('network:foo', 'network'), None)

@raises(requests.exceptions.Timeout)
def test_navitia_timeout():
    n = Navitia('http://api.navitia.io', 'jdr')
    with HTTMock(navitia_mock_timeout):
        n.get_pt_object('network:foo','network')
