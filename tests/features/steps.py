from lettuce import *
from nose.tools import *
import json

def pythonify(value):
    if value.isdigit():
        return int(value)
    return value

def find_field(json, fields):
    seppareted_fields = fields.split('.')
    current_node = json
    for field in seppareted_fields:
        current_node = current_node[field]
    return current_node

@step(u'When I POST to "([^"]+)"')
def when_i_post_to(step, url):
    data = None
    headers = None
    if hasattr(world, 'request_data'):
        data = world.request_data
    if hasattr(world, 'request_headers'):
        headers = world.request_headers
    world.response = world.client.post(url, data=data, headers=headers)

@step(u'Then the status code should be "(\d+)"')
def then_the_status_code_should_be(step, status_code):
    eq_(world.response.status_code, int(status_code))

@step(u'Given I provide this json:')
def given_i_have_this_json(step):
    world.request_data = step.multiline

@step(u'And I set the header "([^"]*)" to "([^"]*)"')
def and_i_set_the_header_to(step, header, value):
    if not hasattr(world, 'request_headers'):
        world.request_headers = {}

    world.request_headers[header] = value

@step(u'And the header "([^"]*)" should contain the value "([^"]*)"')
def and_the_header_is_set_to(step, header, value):
    eq_(world.response.headers[header], value)

@step(u'And the field "([^"]*)" should contain the value "([^"]*)"')
def and_in_the_json_the_field_is_set_to(step, fields, value):
    value = pythonify(value)
    if not hasattr(world, 'reponse_json'):
        world.response_json = json.loads(world.response.get_data())
    eq_(find_field(world.response_json, fields), value)

@step(u'And the field "([^"]*)" should be null')
def and_in_the_json_the_field_is_set_to(step, fields):
    if not hasattr(world, 'reponse_json'):
        world.response_json = json.loads(world.response.get_data())
    eq_(find_field(world.response_json, fields), None)
