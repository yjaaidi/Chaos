from nose.tools import *
from chaos.utils import ParseError
from jsonschema import validate, ValidationError
from chaos.formats import impact_input_format, channel_input_format, severity_input_format,\
    cause_input_format, disruptions_input_format


def test_wording_is_required_in_severity():
    try:
        validate({}, severity_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'wording' is a required property", True)


def test_wording_is_required_in_cause():
    try:
        validate({}, cause_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'wording' is a required property", True)


def test_name_is_required_in_channel():
    try:
        validate({"max_size": 500, "content_type": "text/type"}, channel_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'name' is a required property", True)


def test_max_size_is_required_in_channel():
    try:
        validate({"name": "sms", "content_type": "text/type"}, channel_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'max_size' is a required property", True)


def test_content_type_is_required_in_channel():
    try:
        validate({"name": "sms", "max_size": 500}, channel_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'content_type' is a required property", True)


def test_reference_is_required_in_disruption():
    try:
        validate({"note": "hello", "cause":{"id": "7ffab230-3d48-4eea-aa2c-22f8680230b6"}}, disruptions_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'reference' is a required property", True)


def test_cause_is_required_in_disruption():
    try:
        validate({"reference": "foo", "note": "hello"}, disruptions_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'cause' is a required property", True)


def test_severity_is_required_in_impcat():
    try:
        validate({"application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"},{"begin": "2014-04-29T16:52:00Z","end": "2014-05-22T02:15:00Z"}]}, impact_input_format)
        assert False
    except ValidationError, e:
        eq_(ParseError(e), "'severity' is a required property", True)

