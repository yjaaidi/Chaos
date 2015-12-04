from nose.tools import *
from chaos.utils import get_traffic_report_objects
import chaos
from mock import MagicMock


class Obj(object):
    pass


def test_get_traffic_report_objects():
    dd = get_traffic_report_objects([], Obj())
    eq_(len(dd.items()), 0)


def test_get_traffic_report_without_objects():
    impact = chaos.models.Impact()
    dd = get_traffic_report_objects([impact], Obj())
    eq_(len(dd.items()), 0)


def test_get_traffic_report_with_network():
    impact = chaos.models.Impact()
    navitia = chaos.navitia.Navitia('url', 'cov')
    navitia.get_pt_object = MagicMock(return_value={"id": "uri1", "name": "network name"})
    network = chaos.models.PTobject()
    network.type = 'network'
    network.uri = 'uri1'
    impact.objects.append(network)
    result = {
        "uri1": {
            "network": {
                "id": "uri1",
                "name": "network name"
            }
        }
    }
    dd = get_traffic_report_objects([impact], navitia)
    eq_(cmp(dd, result), 0)
