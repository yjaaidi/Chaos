from nose.tools import *
from chaos import formats
from chaos.utils import get_application_periods_by_pattern, get_application_periods
from jsonschema import validate, ValidationError
from aniso8601 import parse_datetime



#start_date and end_date are on same day with pattern=1111111
def test_pattern_with_one_period_in_result():
    start_date = parse_datetime("2015-02-01T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-01T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 1)

#start_date and end_date are same with pattern=0000000
def test_pattern_with_weekly_pattern_all_off():
    start_date = parse_datetime("2015-02-01T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-01T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "0000000"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 0)

#start_date is greater then end_date
def test_pattern_with_start_date_greater_than_end_date():
    start_date = parse_datetime("2015-02-02T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-01T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 0)

@raises(ValidationError)
def test_pattern_with_wrong_time_slots():
    application_period_pattern = {"start_date": "2015-02-01T06:52:00Z", "end_date": "2015-02-01T23:52:00Z", "weekly_pattern": "0000000"}
    validate(application_period_pattern, formats.pattern_input_format)
    app_periods = get_application_periods_by_pattern(application_period_pattern)
    eq_(len(app_periods), 0)

def test_pattern_with_multi_periods_in_result():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-02-02T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-15T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 14)
    eq_(app_periods[0][0].strftime(date_format), "2015-02-02T06:45:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-02-02T08:30:00Z")
    eq_(app_periods[13][0].strftime(date_format), "2015-02-15T06:45:00Z")
    eq_(app_periods[13][1].strftime(date_format), "2015-02-15T08:30:00Z")


def test_pattern_with_weekly_pattern_all_on_multi_time_slots():
    start_date = parse_datetime("2015-02-01T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-01T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "07:45", "end": "09:30"}, {"begin": "17:45", "end": "19:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 2)

def test_pattern_with_multi_patterns():
    json_impact = {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"},"application_period_patterns":[{"start_date":"2015-02-01","end_date":"2015-02-03","weekly_pattern":"1111111","time_zone":"Europe/Paris","time_slots":[{"begin": "08:45", "end": "09:30"}]},{"start_date":"2015-02-05","end_date":"2015-02-06","weekly_pattern":"1111111","time_zone":"Europe/Paris","time_slots":[{"begin": "17:45", "end": "19:30"}]}]}
    validate(json_impact, formats.impact_input_format)
    app_periods = get_application_periods(json_impact)
    eq_(len(app_periods), 5)

def test_pattern_with_start_date_greater_than_end_date():
    start_date = parse_datetime("2015-02-15T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-02T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 0)

def test_pattern_with_weekend_pattern():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-02-02T06:52:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-02-15T23:52:00Z").replace(tzinfo=None)
    weekly_pattern = "0000011"
    time_slots = [{"begin": "07:45", "end": "09:30"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 4)
    eq_(app_periods[0][0].strftime(date_format), "2015-02-07T06:45:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-02-07T08:30:00Z")
    eq_(app_periods[1][0].strftime(date_format), "2015-02-08T06:45:00Z")
    eq_(app_periods[1][1].strftime(date_format), "2015-02-08T08:30:00Z")
    eq_(app_periods[2][0].strftime(date_format), "2015-02-14T06:45:00Z")
    eq_(app_periods[2][1].strftime(date_format), "2015-02-14T08:30:00Z")
    eq_(app_periods[3][0].strftime(date_format), "2015-02-15T06:45:00Z")
    eq_(app_periods[3][1].strftime(date_format), "2015-02-15T08:30:00Z")

def test_pattern_midnight_change_one_day():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "18:00", "end": "03:00"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 1)
    eq_(app_periods[0][0].strftime(date_format), "2015-09-21T16:00:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-09-22T01:00:00Z")

def test_pattern_midnight_change_one_day_one_oclock():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    weekly_pattern = "1111111"
    time_slots = [{"begin": "18:00", "end": "01:00"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 1)
    eq_(app_periods[0][0].strftime(date_format), "2015-09-21T16:00:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-09-21T23:00:00Z")

def test_pattern_midnight_change_several_days_with_last_day_not_valid():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-09-26T00:00:00Z").replace(tzinfo=None)
    weekly_pattern = "1101001"
    time_slots = [{"begin": "18:00", "end": "03:00"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 3)
    eq_(app_periods[0][0].strftime(date_format), "2015-09-21T16:00:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-09-22T01:00:00Z")
    eq_(app_periods[1][0].strftime(date_format), "2015-09-22T16:00:00Z")
    eq_(app_periods[1][1].strftime(date_format), "2015-09-23T01:00:00Z")
    eq_(app_periods[2][0].strftime(date_format), "2015-09-24T16:00:00Z")
    eq_(app_periods[2][1].strftime(date_format), "2015-09-25T01:00:00Z")

def test_pattern_midnight_change_several_days_with_last_day_valid():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-09-21T00:00:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-09-26T00:00:00Z").replace(tzinfo=None)
    weekly_pattern = "1101010"
    time_slots = [{"begin": "18:00", "end": "03:00"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 4)
    eq_(app_periods[0][0].strftime(date_format), "2015-09-21T16:00:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-09-22T01:00:00Z")
    eq_(app_periods[1][0].strftime(date_format), "2015-09-22T16:00:00Z")
    eq_(app_periods[1][1].strftime(date_format), "2015-09-23T01:00:00Z")
    eq_(app_periods[2][0].strftime(date_format), "2015-09-24T16:00:00Z")
    eq_(app_periods[2][1].strftime(date_format), "2015-09-25T01:00:00Z")
    eq_(app_periods[3][0].strftime(date_format), "2015-09-26T16:00:00Z")
    eq_(app_periods[3][1].strftime(date_format), "2015-09-27T01:00:00Z")

def test_pattern_midnight_change_several_days_with_last_day_valid_():
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    start_date = parse_datetime("2015-09-22T00:00:00Z").replace(tzinfo=None)
    end_date = parse_datetime("2015-09-24T00:00:00Z").replace(tzinfo=None)
    weekly_pattern = "1110111"
    time_slots = [{"begin": "18:00", "end": "03:00"}]
    app_periods = get_application_periods_by_pattern(start_date, end_date, weekly_pattern, time_slots, 'Europe/Paris')
    eq_(len(app_periods), 2)
    eq_(app_periods[0][0].strftime(date_format), "2015-09-22T16:00:00Z")
    eq_(app_periods[0][1].strftime(date_format), "2015-09-23T01:00:00Z")
    eq_(app_periods[1][0].strftime(date_format), "2015-09-23T16:00:00Z")
    eq_(app_periods[1][1].strftime(date_format), "2015-09-24T01:00:00Z")
