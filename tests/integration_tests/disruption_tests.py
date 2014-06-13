import chaos
from nose.tools import eq_
import helpers
import json

#Caution order is important, test are run by alphabetical order

class TestDisruption(object):

    disruption_id = None

    @classmethod
    def setup_class(cls):
        helpers.setup_db()

    @classmethod
    def teardown_class(cls):
        helpers.teardown_db()

    def test_1_empty(self):
        client = chaos.app.test_client()
        resp = client.get('/disruptions')
        eq_(resp.status_code, 200)
        eq_(resp.headers['content-type'], 'application/json')
        data = json.loads(resp.get_data())
        assert 'disruptions' in data
        eq_(len(data['disruptions']), 0)


    def test_2_post(self):
        data = {'reference': 'foo', 'note': 'bar'}
        client = chaos.app.test_client()
        resp = client.post('/disruptions',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(data))
        eq_(resp.status_code, 201)
        eq_(resp.headers['content-type'], 'application/json')
        disruption = json.loads(resp.get_data())
        assert 'disruption' in disruption
        eq_(disruption['disruption']['reference'], 'foo')
        eq_(disruption['disruption']['note'], 'bar')
        eq_(disruption['disruption']['status'], 'published')
        assert 'id' in disruption['disruption']
        assert 'self' in disruption['disruption']
        TestDisruption.disruption_id = disruption['disruption']['id']
        eq_(disruption['disruption']['self']['href'], 'http://localhost/disruptions/{}'.format(TestDisruption.disruption_id))

    def test_3_list(self):
        client = chaos.app.test_client()
        resp = client.get('/disruptions')
        eq_(resp.status_code, 200)
        eq_(resp.headers['content-type'], 'application/json')
        data = json.loads(resp.get_data())
        assert 'disruptions' in data
        eq_(len(data['disruptions']), 1)

    def test_3_get_one(self):
        client = chaos.app.test_client()
        resp = client.get('/disruptions/{}'.format(TestDisruption.disruption_id))
        eq_(resp.status_code, 200)
        eq_(resp.headers['content-type'], 'application/json')
        disruption = json.loads(resp.get_data())
        assert 'disruption' in disruption
        eq_(disruption['disruption']['reference'], 'foo')
        eq_(disruption['disruption']['note'], 'bar')
        eq_(disruption['disruption']['status'], 'published')
        assert 'id' in disruption['disruption']
        assert 'self' in disruption['disruption']
        eq_(disruption['disruption']['self']['href'], 'http://localhost/disruptions/{}'.format(TestDisruption.disruption_id))

    def test_4_put(self):
        data = {'reference': 'reference', 'note': 'note'}
        client = chaos.app.test_client()
        resp = client.put('/disruptions/{}'.format(TestDisruption.disruption_id),
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(data))
        eq_(resp.status_code, 200)
        eq_(resp.headers['content-type'], 'application/json')
        disruption = json.loads(resp.get_data())
        assert 'disruption' in disruption
        eq_(disruption['disruption']['reference'], 'reference')
        eq_(disruption['disruption']['note'], 'note')
        eq_(disruption['disruption']['status'], 'published')

    def test_5_delete(self):
        client = chaos.app.test_client()
        resp = client.delete('/disruptions/{}'.format(TestDisruption.disruption_id))
        eq_(resp.status_code, 204)
        eq_(resp.get_data(), '')

    def test_6_list_empty(self):
        self.test_1_empty()

