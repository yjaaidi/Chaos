from os import path
import json
from nose.tools import *
from nose import with_setup
from chaos.utils import client_token_is_allowed

correct_file =  path.dirname(path.realpath(__file__)) + '/fixtures/clients_tokens.json'
wrong_file =  path.dirname(path.realpath(__file__)) + '/fixtures/foo.json'

def test_client_token_file_doesnt_exist():
    assert client_token_is_allowed('transilien', '9bf5', wrong_file)

def test_client_with_first_token_is_allowed():
    assert client_token_is_allowed('transilien', '9bf5', correct_file)

def test_client_with_second_token_is_allowed():
    assert client_token_is_allowed('transilien', '9bf6', correct_file)

@raises(ValueError)
def test_client_with_wrong_token_is_not_allowed():
    client_token_is_allowed('transilien', '1', correct_file)

@raises(ValueError)
def test_wrong_client_is_not_allowed():
    client_token_is_allowed('centre', '9bf5', correct_file)

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