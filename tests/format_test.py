
from nose.tools import *
from chaos import formats

from jsonschema import validate, Draft4Validator, ValidationError

def test_validate_date_period_format():
    Draft4Validator.check_schema(formats.date_period_format)

def test_validate_disruption_format():
    Draft4Validator.check_schema(formats.disruptions_input_format)

def test_validate_severity_format():
    Draft4Validator.check_schema(formats.severity_input_format)

def test_validate_cause_format():
    Draft4Validator.check_schema(formats.cause_input_format)

def test_severities_validation():
    json = {'wording': 'foo', 'color': 'a'*20}
    validate(json, formats.severity_input_format)

    json['priority'] = 2
    validate(json, formats.severity_input_format)

    json['effect'] = None
    validate(json, formats.severity_input_format)

@raises(ValidationError)
def test_severities_validation_color_has_max_length():
    json = {'wording': 'foo', 'color': 'a'*21}
    validate(json, formats.severity_input_format)

@raises(ValidationError)
def test_severities_validation_wording_has_max_length():
    json = {'wording': 'a'*251}
    validate(json, formats.severity_input_format)

@raises(ValidationError)
def test_severities_validation_wording_is_required():
    json = {'color': 'aa'}
    validate(json, formats.severity_input_format)

def test_severities_validation_effect_can_be_null_or_blocking():
    json = {'wording': 'aa', 'effect': None}
    validate(json, formats.severity_input_format)

    json = {'wording': 'aa', 'effect': 'blocking'}
    validate(json, formats.severity_input_format)

@raises(ValidationError)
def test_severities_validation_value_of_effect_is_limited():
    json = {'wording': 'aa', 'effect': 'nonblocking'}
    validate(json, formats.severity_input_format)

def test_severities_validation_priority_is_int_or_null():
    json = {'wording': 'aa', 'priority': None}
    validate(json, formats.severity_input_format)

    json = {'wording': 'aa', 'priority': 1}
    validate(json, formats.severity_input_format)

@raises(ValidationError)
def test_severities_validation_is_int_or_null_2():
    json = {'wording': 'aa', 'priority': '1'}
    validate(json, formats.severity_input_format)

def test_causes_validation():
    json = {'wording': 'foo'}
    validate(json, formats.cause_input_format)

    json = {'wording': 'a'*250}
    validate(json, formats.cause_input_format)


@raises(ValidationError)
def test_causes_validation_wording_is_required():
    json = {}
    validate(json, formats.cause_input_format)

@raises(ValidationError)
def test_causes_validation_wording_has_max_length():
    json = {'wording': 'a'*251}
    validate(json, formats.cause_input_format)

def test_validate_channel_format():
    Draft4Validator.check_schema(formats.channel_input_format)

def test_channels_validation():
    json = {'name': 'short', 'max_size': 200, 'content_type': 'text/plain'}
    validate(json, formats.channel_input_format)

    json = {'name': 'short', 'max_size': 200, 'content_type': ''}
    validate(json, formats.channel_input_format)

@raises(ValidationError)
def test_channel_validation_attributs_mandatory():
    json = {'name': 'short', 'max_size': 200}
    validate(json, formats.channel_input_format)


@raises(ValidationError)
def test_channel_validation_name_has_max_length():
    json = {'name': 's'*251, 'max_size': 200, 'content_type': 'text/plain'}
    validate(json, formats.channel_input_format)
