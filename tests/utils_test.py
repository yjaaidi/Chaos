from os import path
import json
from nose.tools import *
from nose import with_setup
from chaos.utils import client_token_is_allowed

correct_file =  path.dirname(path.realpath(__file__)) + '/fixtures/clients_tokens.json'
wrong_file =  path.dirname(path.realpath(__file__)) + '/fixtures/foo.json'

@raises(ValueError)
def test_client_token_file_doesnt_exist():
    clients_tokens = get_clients_tokens_from_file(wrong_file)
    assert client_token_is_allowed('transilien', '9bf5', clients_tokens)

def test_client_with_first_token_is_allowed():
    clients_tokens = get_clients_tokens_from_file(correct_file)
    assert client_token_is_allowed('transilien', '9bf5', clients_tokens)

def test_client_with_second_token_is_allowed():
    clients_tokens = get_clients_tokens_from_file(correct_file)
    assert client_token_is_allowed('transilien', '9bf6', clients_tokens)

@raises(ValueError)
def test_client_with_wrong_token_is_not_allowed():
    clients_tokens = get_clients_tokens_from_file(correct_file)
    client_token_is_allowed('transilien', '1', clients_tokens)

@raises(ValueError)
def test_wrong_client_is_not_allowed():
    clients_tokens = get_clients_tokens_from_file(correct_file)
    client_token_is_allowed('centre', '9bf5', clients_tokens)

def get_clients_tokens_from_file(file_name):
    """
    Retrieves parsed json file content as dict
    :param file_name: File path to parse
    :return: parsed file content as dict
    """
    clients_tokens = {}

    if path.exists(file_name):
        with open(file_name, 'r') as f:
            clients_tokens = json.load(f)

    return clients_tokens