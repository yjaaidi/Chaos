from nose.tools import *
from chaos.utils import is_valid_ids
from chaos.exceptions import InvalidId


def test_valid_id():
    ids = ["7ffab230-3d48-4eea-aa2c-22f8680230b6", "3ffab232-3d48-4eea-aa2c-22f8680230b6"]
    is_valid_ids(ids)
    eq_(is_valid_ids(ids), True)


@raises(InvalidId)
def test_invalid_id():
    ids = ["7ffab230-3d48-4eea-aa2c-22f8680230b6", "AA"]
    is_valid_ids(ids)

