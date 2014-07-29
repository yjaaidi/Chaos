from nose.tools import *
from chaos.utils import parse_error

import chaos

class Obj(object):
    pass


def test_error_with_message():
    error = Obj()
    error.message = 'message'
    eq_(parse_error(error), 'message', True)


def test_error_without_message():
    error = Obj()
    error.message = 'aa \n bbb \n c'
    eq_(parse_error(error.message), 'aa   bbb   c', True)