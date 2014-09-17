from nose.tools import *
import chaos
from chaos.populate_pb import PopulatePb
from aniso8601 import parse_datetime


def get_disruption():

    # Disruption
    disruption = chaos.models.Disruption()
    disruption.cause = chaos.models.Cause()
    disruption.cause.wording = "CauseTest"
    disruption.reference = "DisruptionTest"
    disruption.localization_id = "123"

    # Tag
    tag = chaos.models.Tag()
    tag.name = "rer"
    disruption.tags.append(tag)
    tag = chaos.models.Tag()
    tag.name = "metro"
    disruption.tags.append(tag)

    # Impacts
    impact = chaos.models.Impact()
    impact.severity = chaos.models.Severity()
    impact.severity.wording = "SeverityTest"
    impact.severity.color = "#FFFF00"

    # ApplicationPeriods
    application_period = chaos.models.ApplicationPeriods()
    application_period.start_date = parse_datetime("2014-04-12T16:52:00").replace(tzinfo=None)
    application_period.end_date = parse_datetime("2015-04-12T16:52:00").replace(tzinfo=None)
    impact.application_periods.append(application_period)

    # PTobject
    ptobject = chaos.models.PTobject()
    ptobject.uri = "stop_area:123"
    ptobject.type = "stop_area"
    impact.objects.append(ptobject)

    ptobject = chaos.models.PTobject()
    ptobject.uri = "line:123"
    ptobject.type = "line"
    impact.objects.append(ptobject)

    # Messages
    message = chaos.models.Message()
    message.text = "Meassage1 test"
    message.channel = chaos.models.Channel()
    message.channel.name = "sms"
    message.channel.max_size = 60
    message.channel.content_type = "text"
    impact.messages.append(message)

    message = chaos.models.Message()
    message.text = "Meassage2 test"
    message.channel = chaos.models.Channel()
    message.channel.name = "email"
    message.channel.max_size = 250
    message.channel.content_type = "html"
    impact.messages.append(message)

    disruption.impacts.append(impact)

    return disruption


def test_disruption():
    disruption = get_disruption()
    pb = PopulatePb(disruption)
    pb.populate()
    eq_(pb.feed_entity.is_deleted, False)
    eq_(pb.extend_feed_entity.reference,  disruption.reference)
    eq_(pb.extend_feed_entity.cause.wording,  disruption.cause.wording)
    eq_(len(pb.extend_feed_entity.localization),  1)
    eq_(pb.extend_feed_entity.localization[0].stop_id,  disruption.localization_id)
    eq_(len(pb.extend_feed_entity.tags),  2)
    eq_(pb.extend_feed_entity.tags[0].name,  disruption.tags[0].name)
    eq_(pb.extend_feed_entity.tags[1].name,  disruption.tags[1].name)


    eq_(len(pb.extend_feed_entity.impacts),  1)
    eq_(pb.extend_feed_entity.impacts[0].severity.wording,  "SeverityTest")
    eq_(pb.extend_feed_entity.impacts[0].severity.color,  "#FFFF00")

    eq_(len(pb.extend_feed_entity.impacts[0].application_periods),  1)
    eq_(len(pb.extend_feed_entity.impacts[0].informed_entities),  2)

    eq_(pb.extend_feed_entity.impacts[0].informed_entities[0].uri,  disruption.impacts[0].objects[0].uri)
    eq_(pb.extend_feed_entity.impacts[0].informed_entities[0].pt_object_type,  pb.get_pt_object_type(disruption.impacts[0].objects[0].type))

    eq_(pb.extend_feed_entity.impacts[0].informed_entities[1].uri,  disruption.impacts[0].objects[1].uri)
    eq_(pb.extend_feed_entity.impacts[0].informed_entities[1].pt_object_type,  pb.get_pt_object_type(disruption.impacts[0].objects[1].type))

    eq_(pb.extend_feed_entity.impacts[0].messages[0].text,  disruption.impacts[0].messages[0].text)
    eq_(pb.extend_feed_entity.impacts[0].messages[0].channel.name,  disruption.impacts[0].messages[0].channel.name)
    eq_(pb.extend_feed_entity.impacts[0].messages[0].channel.max_size,  disruption.impacts[0].messages[0].channel.max_size)
    eq_(pb.extend_feed_entity.impacts[0].messages[0].channel.content_type,  disruption.impacts[0].messages[0].channel.content_type)

    eq_(pb.extend_feed_entity.impacts[0].messages[1].text,  disruption.impacts[0].messages[1].text)
    eq_(pb.extend_feed_entity.impacts[0].messages[1].channel.name,  disruption.impacts[0].messages[1].channel.name)
    eq_(pb.extend_feed_entity.impacts[0].messages[1].channel.max_size,  disruption.impacts[0].messages[1].channel.max_size)
    eq_(pb.extend_feed_entity.impacts[0].messages[1].channel.content_type,  disruption.impacts[0].messages[1].channel.content_type)

def test_disruption_is_deleted():
    disruption = get_disruption()
    disruption.status = 'archived'
    pb = PopulatePb(disruption, disruption.status == 'archived')
    pb.populate()
    eq_(pb.feed_entity.is_deleted, True)

@raises(AttributeError)
def test_disruption_with_impact_without_severity():
    disruption = get_disruption()
    del disruption.impacts[0].severity
    pb = PopulatePb(disruption)
    pb.populate()



@raises(AttributeError)
def test_disruption_without_cause():
    disruption = get_disruption()
    del disruption.cause
    pb = PopulatePb(disruption)
    pb.populate()
