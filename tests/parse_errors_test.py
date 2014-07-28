from nose.tools import *
from chaos.utils import ParseError

import chaos

class Obj(object):
    pass


def test_error_with_message():
    error = Obj()
    error.message = 'message'
    eq_(ParseError(error), 'message', True)


def test_error_without_message():
    error = Obj()
    error.message = 'aa \n bbb \n c'
    eq_(ParseError(error.message), 'aa   bbb   c', True)