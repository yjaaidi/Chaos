
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

def test_validate_object_format():
    Draft4Validator.check_schema(formats.object_input_format)

def test_object_validation():
    json = {'id': 'stop_area:...:200', 'type': 'network'}
    validate(json, formats.object_input_format)

@raises(ValidationError)
def test_object_validation_without_type():
    json = {'id': 'stop_area:...:200'}
    validate(json, formats.object_input_format)

@raises(ValidationError)
def test_object_validation_id_has_max_length():
    json = {'id': 's'*251, 'type': 'network'}
    validate(json, formats.object_input_format)

def test_validate_impact_format():
    Draft4Validator.check_schema(formats.impact_input_format)

def test_impact_without_application_period_validation():
    json = {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},
            "objects": [{"id": "stop_area:RTP:SA:3786125","type": "network"},{"id": "line:RTP:LI:378","type": "network"}]}
    validate(json, formats.impact_input_format)

def test_impact_without_object_validation():
    json = {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},
            "application_periods": [{"begin": "2014-06-20T17:00:00Z","end":"2014-07-28T17:00:00Z"}]}
    validate(json, formats.impact_input_format)

def test_impact_with_object_and_application_period_validation():
    json = {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},
            "application_periods": [{"begin": "2014-06-20T17:00:00Z","end":"2014-07-28T17:00:00Z"}],
            "objects": [{"id": "stop_area:RTP:SA:3786125","type": "network"},{"id": "line:RTP:LI:378","type": "network"}]
            }
    validate(json, formats.impact_input_format)

@raises(ValidationError)
def test_impact_without_severity_validation():
    json = {"application_periods": [{"begin": "2014-06-20T17:00:00Z","end":"2014-07-28T17:00:00Z"}],
            "objects": [{"id": "stop_area:RTP:SA:3786125","type": "network"},{"id": "line:RTP:LI:378","type": "network"}]
            }
    validate(json, formats.impact_input_format)
