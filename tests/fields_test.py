from nose.tools import *
from chaos import fields, models, app
from datetime import datetime, time
from flask import g


class Obj(object):
    pass


def test_field_object_name_None():
    class_field_object_name = fields.FieldObjectName(Obj())
    eq_(class_field_object_name.output(None, None), None)


def test_field_contributor_None():
    class_field_contributor = fields.FieldContributor(Obj())
    eq_(class_field_contributor.output(None, None), None)


def test_field_links_None():
    class_field_links = fields.FieldLinks(Obj())
    test = {}
    eq_(class_field_links.output(None, test), None)


def test_none_field_date_time():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format(None), None)

@raises(AttributeError)
def test_field_date_time_invalid():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format('2014-08-07 12:46:56.837613'), None)


def test_field_date_time_valid():
    class_datetime = fields.FieldDateTime(Obj())
    eq_(class_datetime.format(datetime(2014, 2, 10, 13, 5, 10)), '2014-02-10T13:05:10Z')


def test_name_channel():
    channel = models.Channel()
    eq_(str(channel), "<Channel '{}'>".format(channel.id))


def test_name_impact():
    impact = models.Impact()
    eq_(str(impact), "<Impact '{}'>".format(impact.id))


def test_name_disruption():
    disruption = models.Disruption()
    eq_(str(disruption), "<Disruption '{}'>".format(disruption.id))


def test_none_field_time():
    class_time = fields.FieldTime(Obj())
    eq_(class_time.format(None), None)


def test_field_time_invalid():
    class_time = fields.FieldTime(Obj())
    eq_(class_time.format('12:46'), None)


def test_field_time_valid():
    class_time = fields.FieldTime(Obj())
    eq_(class_time.format(time(hour=13, minute=5)), '13:05')

# disruption.status : future
'''
application_period              2014-02-10                                  2014-03-10
current date        2014-01-10
'''
def test_future_status_disruption():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 10, 13, 5, 10)
    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)
    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 1, 10, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'future')


# disruption.status : activate
'''
application_period              2014-02-10                                  2014-03-10
current date                                        2014-02-11
'''
def test_activate_status_disruption():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 10, 13, 5, 10)
    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)
    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 2, 11, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'active')

# disruption.status : past
'''
application_period              2014-02-10                    2014-03-10
current date                                                                                2014-03-11
'''
def test_past_status_disruption():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 10, 13, 5, 10)
    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)
    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 3, 11, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'past')

# disruption.status : future
'''
application_period              2014-02-10                   2014-03-10
application_period                                                                  2014-03-12                014-03-15
current date        2014-01-10
'''
def test_future_status_disruption_2_periods():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 16, 13, 5, 10)

    impact = models.Impact()

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 3, 12, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 15, 13, 5, 10)
    impact.application_periods.append(application_period)

    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 1, 10, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'future')

# disruption.status : activate
'''
application_period              2014-02-10                             2014-03-10
application_period                                                                  2014-03-12                2014-03-15
current date                                        2014-02-11
'''
def test_activate_disruption_2_periods():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 16, 13, 5, 10)

    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 3, 12, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 15, 13, 5, 10)
    impact.application_periods.append(application_period)

    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 2, 11, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'active')

# disruption.status : future
'''
application_period              2014-02-10                2014-03-10
application_period                                                                    2014-03-12       014-03-15
current date                                                            2014-03-11
'''
def test_future_disruption_2_periods():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 16, 13, 5, 10)
    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 3, 12, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 15, 13, 5, 10)
    impact.application_periods.append(application_period)

    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 3, 11, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'future')

# disruption.status : activate
'''
application_period              2014-02-10          2014-03-10
application_period                                                    2014-03-12                    2014-03-15
current date                                                                        2014-03-13
'''
def test_activate_disruption_2_periods_1():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 16, 13, 5, 10)

    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 3, 12, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 15, 13, 5, 10)
    impact.application_periods.append(application_period)

    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 3, 13, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'active')

# disruption.status : past
'''
application_period          2014-02-10     2014-03-10
application_period                                         2014-03-12        2014-03-15
current date                                                                                2014-03-16
'''
def test_past_disruption_2_periods():
    disruption = models.Disruption()
    disruption.start_publication_date = datetime(2014, 2, 10, 13, 5, 10)
    disruption.end_publication_date = datetime(2014, 3, 16, 13, 5, 10)

    impact = models.Impact()
    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 2, 10, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 10, 13, 5, 10)
    impact.application_periods.append(application_period)

    application_period = models.ApplicationPeriods()
    application_period.start_date = datetime(2014, 3, 12, 13, 5, 10)
    application_period.end_date = datetime(2014, 3, 15, 13, 5, 10)
    impact.application_periods.append(application_period)

    disruption.impacts.append(impact)
    impact.disruption = disruption
    with app.app_context():
        g.current_time = datetime(2014, 3, 16, 13, 5, 10)
        class_time = fields.ComputeDisruptionStatus(Obj())
        eq_(class_time.output(None, impact), 'past')


def test_field_cause():
    obj = Obj()
    obj.disruption = models.Disruption()
    cause = models.Cause()
    wording = models.Wording()
    wording.key = 'external_medium'
    wording.value = 'external medium'
    cause.wordings.append(wording)
    obj.disruption.cause = cause
    class_field_cause = fields.FieldCause(Obj())
    eq_(class_field_cause.output(None, obj), 'external medium')


def test_field_cause_none():
    obj = Obj()
    obj.disruption = models.Disruption()
    cause = models.Cause()
    wording = models.Wording()
    wording.key = 'external_long'
    wording.value = 'external medium'
    cause.wordings.append(wording)
    obj.disruption.cause = cause
    class_field_cause = fields.FieldCause(Obj())
    eq_(class_field_cause.output(None, obj), None)
