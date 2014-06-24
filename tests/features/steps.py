from lettuce import *
from nose.tools import *
import json
from chaos import db
from chaos.models import Disruption

def pythonify(value):
    if value.isdigit():
        return int(value)
    return value

def find_field(json, fields):
    seppareted_fields = map(pythonify, fields.split('.'))
    current_node = json
    for field in seppareted_fields:
        current_node = current_node[field]
    return current_node

@step(u'I (\w+) (?:to\s)?"([^"]+)"(?:\swith:)?')
def when_i_post_to(step, method, url):
    if step.multiline:
        data = step.multiline
    else:
        data = None
    headers = {'content-type': 'application/json'}
    world.response = world.client.open(path=url, method=method, data=data, headers=headers)

@step(u'Then the status code should be "(\d+)"')
def then_the_status_code_should_be(step, status_code):
    eq_(world.response.status_code, int(status_code))

@step(u'And the header "([^"]*)" should be "([^"]*)"')
def and_the_header_is_set_to(step, header, value):
    eq_(world.response.headers[header], value)

@step(u'And the field "([^"]*)" should be "([^"]*)"')
def and_in_the_json_the_field_is_set_to(step, fields, value):
    value = pythonify(value)
    eq_(find_field(world.response_json, fields), value)

@step(u'And the field "([^"]*)" should be null')
def and_in_the_json_the_field_is_set_to(step, fields):
    eq_(find_field(world.response_json, fields), None)

@step(u'and "([^"]*)" should be empty')
def and_field_should_be_empty(step, fields):
    assert_equals(len(find_field(world.response_json, fields)), 0)

@step(u'Given I have the folowing disruptions in my database:')
def given_i_have_the_folowing_disruptions_in_my_database(step):
    for disruption_dict in step.hashes:
        disruption = Disruption()
        for key, value in disruption_dict.iteritems():
            if value == 'None':
                value = None
            setattr(disruption, key, value)
        db.session.add(disruption)
    db.session.commit()

@step(u'And the field "([^"]*)" should have a size of (\d+)')
def and_the_field_should_have_a_size_of_n(step, fields, size):
    eq_(len(find_field(world.response_json, fields)), int(size))

