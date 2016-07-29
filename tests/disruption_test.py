import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
from nose.tools import assert_false, eq_
from chaos import models
from chaos.utils import send_disruption_to_navitia

def test_disruption_with_draft_status_isnnot_send():
    '''
    Tests that a disruption with status draft is not sent to navitia
    :return:
    '''
    disruption = models.Disruption()
    disruption.status = 'draft'
    hasBeenSent = send_disruption_to_navitia(disruption)

    eq_(hasBeenSent, False)

def test_disruption_with_archived_status_is_sent():
    '''
    Tests that a disruption with status archived is sent to navitia
    :return:
    '''
    disruption = models.Disruption()

    disruption.contributor = models.Contributor()
    disruption.contributor_id = disruption.contributor.id

    disruption.status = 'archived'
    hasBeenSent = send_disruption_to_navitia(disruption)

    eq_(hasBeenSent, None)

def test_disruption_with_published_status_is_sent():
    '''
    Tests that a disruption with status published is sent to navitia
    :return:
    '''
    disruption = models.Disruption()

    #contributor
    disruption.contributor = models.Contributor()
    disruption.contributor_id = disruption.contributor.id

    #cause
    disruption.cause = models.Cause()
    disruption.cause.wording = "CauseTest"
    disruption.cause.category = models.Category()
    disruption.cause.category.name = "CategoryTest"
    disruption.reference = "DisruptionTest"

    #localization
    localization = models.PTobject()
    localization.uri = "stop_area:123"
    localization.type = "stop_area"
    disruption.localizations.append(localization)

    # Wording
    wording = models.Wording()
    wording.key = "key_1"
    wording.value = "value_1"
    disruption.cause.wordings.append(wording)
    wording = models.Wording()
    wording.key = "key_2"
    wording.value = "value_2"
    disruption.cause.wordings.append(wording)

    # Tag
    tag = models.Tag()
    tag.name = "rer"
    disruption.tags.append(tag)

    disruption.status = 'published'
    hasBeenSent = send_disruption_to_navitia(disruption)

    eq_(hasBeenSent, None)