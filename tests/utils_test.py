from os import path
from nose.tools import *
from datetime import datetime, timedelta
from chaos.utils import client_token_is_allowed, get_clients_tokens, add_notification_date_on_impacts, \
    define_notification_date_for_impact
from chaos.exceptions import Unauthorized

correct_file_with_master_key = path.dirname(path.realpath(__file__)) + '/fixtures/clients_tokens.json'
correct_file_without_master_key = path.dirname(path.realpath(__file__)) + '/fixtures/clients_tokens.json'
wrong_file = path.dirname(path.realpath(__file__)) + '/fixtures/foo.json'


def test_client_token_file_doesnt_exist():
    assert get_clients_tokens(wrong_file) == None


def test_client_with_first_token_is_allowed():
    clients_tokens = get_clients_tokens(correct_file_with_master_key)
    assert client_token_is_allowed(clients_tokens, 'transilien', '9bf5')
    clients_tokens = get_clients_tokens(correct_file_without_master_key)
    assert client_token_is_allowed(clients_tokens, 'transilien', '9bf5')


def test_client_with_second_token_is_allowed():
    clients_tokens = get_clients_tokens(correct_file_with_master_key)
    assert client_token_is_allowed(clients_tokens, 'transilien', '9bf6')
    clients_tokens = get_clients_tokens(correct_file_without_master_key)
    assert client_token_is_allowed(clients_tokens, 'transilien', '9bf6')


def test_client_with_master_token_is_allowed():
    clients_tokens = get_clients_tokens(correct_file_with_master_key)
    assert client_token_is_allowed(clients_tokens, 'transilien', '42')
    assert client_token_is_allowed(clients_tokens, 'another_one', '42')


@raises(Unauthorized)
def test_client_with_wrong_token_is_not_allowed():
    clients_tokens = get_clients_tokens(correct_file_with_master_key)
    client_token_is_allowed(clients_tokens, 'transilien', '1')
    clients_tokens = get_clients_tokens(correct_file_without_master_key)
    client_token_is_allowed(clients_tokens, 'transilien', '1')


@raises(Unauthorized)
def test_wrong_client_is_not_allowed():
    clients_tokens = get_clients_tokens(correct_file_with_master_key)
    client_token_is_allowed(clients_tokens, 'centre', '9bf5')
    clients_tokens = get_clients_tokens(correct_file_without_master_key)
    client_token_is_allowed(clients_tokens, 'centre', '9bf5')


def test_add_notification_date_on_impacts():
    now = datetime.utcnow().replace(microsecond=0)
    one_day = timedelta(days=1)
    tomorrow = now + one_day
    yesterday = now - one_day

    assert_add_notification_date_on_impacts(yesterday, True, now)
    assert_add_notification_date_on_impacts(yesterday, False, yesterday)
    assert_add_notification_date_on_impacts(now, True, now)
    assert_add_notification_date_on_impacts(now, False, now)
    assert_add_notification_date_on_impacts(tomorrow, True, tomorrow)
    assert_add_notification_date_on_impacts(tomorrow, False, tomorrow)


def assert_add_notification_date_on_impacts(notification_date, send_notifications, expected_date):
    impact = generate_impact(send_notifications, notification_date)

    add_notification_date_on_impacts(impact)

    actual_notification_date = impact["notification_date"]
    assert (format_date(expected_date) == actual_notification_date)


def test_define_notification_date_for_impact():
    now = datetime.utcnow().replace(microsecond=0)
    one_day = timedelta(days=1)
    tomorrow = now + one_day
    yesterday = now - one_day

    assert_notification_date_for_impact(yesterday, now)
    assert_notification_date_for_impact(now, now)
    assert_notification_date_for_impact(tomorrow, tomorrow)


def assert_notification_date_for_impact(notification_date, expected_date):
    """
    Asserts that for given notification_date attribute expected_date is correct
    :param notification_date: string
    :param expected_date: datetime
    :return:
    """
    impact = generate_impact(False, notification_date)
    impact_notification_date = define_notification_date_for_impact(impact)

    assert (expected_date == impact_notification_date)


def generate_impact(send_notifications, notification_date):
    """
    Simulates impacts json representation

    :param send_notifications: Boolean
    :param notification_date: datetime
    :return: dictionary
    """
    return {
        "send_notifications": send_notifications,
        "notification_date": format_date(notification_date)
    }


def format_date(date, format="%Y-%m-%dT%H:%M:%SZ"):
    return datetime.strftime(date, format)
