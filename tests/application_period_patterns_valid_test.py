from nose.tools import *
from chaos import formats
from chaos.utils import get_application_periods_by_pattern, get_application_periods
from jsonschema import validate, ValidationError


#start_date and end_date are on same day with pattern=1111111
def test_pattern_with_one_period_in_result():
    application_period_pattern = {"start_date": "2015-02-01T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "1111111", "time_slots": [{"begin": "07:45", "end": "09:30"}]}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 1)

#start_date and end_date are same with pattern=0000000
def test_pattern_with_weekly_pattern_all_off():
    application_period_pattern = {"start_date": "2015-02-01T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "0000000", "time_slots": [{"begin": "07:45", "end": "09:30"}]}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 0)

#start_date is greater then end_date
def test_pattern_with_start_date_greater_than_end_date():
    application_period_pattern = {"start_date": "2015-02-02T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "1111111", "time_slots": [{"begin": "07:45", "end": "09:30"}]}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 0)

@raises(ValidationError)
def test_pattern_with_wrong_time_slots():
    application_period_pattern = {"start_date": "2015-02-01T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "0000000"}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 0)

#start_date is greater then end_date
def test_pattern_with_multi_periods_in_result():
    application_period_pattern = {"start_date": "2015-02-02T06:52:00Z", "end_date": "2015-02-15T23:52:00Z", "weekly_pattern": "1111111", "time_slots": [{"begin": "07:45", "end": "09:30"}]}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 14)


def test_pattern_with_weekly_pattern_all_on_multi_time_slots():
    application_period_pattern = {"start_date": "2015-02-01T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "1111111", "time_slots": [{"begin": "07:45", "end": "09:30"}, {"begin": "17:45", "end": "19:30"}]}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 2)

def test_pattern_with_multi_patterns():
    json_impact = {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"application_period_patterns":[{"start_date":"2015-02-01T08:52:00Z","end_date":"2015-02-03T16:52:00Z","weekly_pattern":"1111111","time_slots":[{"begin": "08:45", "end": "09:30"}]},{"start_date":"2015-02-05T16:52:00Z","end_date":"2015-02-06T16:52:00Z","weekly_pattern":"1111111","time_slots":[{"begin": "17:45", "end": "19:30"}]}]}
    validate(json_impact, formats.impact_input_format)
    app_periods = get_application_periods(json_impact)
    eq_(len(app_periods), 4)
