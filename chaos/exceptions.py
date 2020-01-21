# Copyright (c) since 2001, Kisio Digital and/or its affiliates. All rights reserved.
from new_relic import record_exception, record_custom_parameter
from flask import request
import logging
from . import VERSION

class ObjectTypeUnknown(Exception):

    def __init__(self, object_type):
        self.message = 'object type {object_type} unknown'.\
            format(object_type=object_type)


class ObjectUnknown(Exception):

    def __init__(self, message=''):
        self.message = message


class HeaderAbsent(Exception):

    def __init__(self, message=''):
        self.message = message


class Unauthorized(Exception):

    def __init__(self, message=''):
        self.message = message


class InvalidJson(Exception):

    def __init__(self, message=''):
        self.message = message


class NavitiaError(Exception):

    def __init__(self, message=''):
        self.message = message

def log_exception(sender, exception, **extra):
    logger = logging.getLogger(__name__)
    message = ""
    if hasattr(exception, "message"):
        message = exception.message
    error = '{} {} {}'.format(exception.__class__.__name__, message, request.url)

    logger.exception(error)
    if 'X-Customer-Id' in request.headers:
        record_custom_parameter('X-Customer-Id', request.headers['X-Customer-Id'])
    if 'X-Contributors' in request.headers:
        record_custom_parameter('X-Contributors', request.headers['X-Contributors'])
    if 'Authorization' in request.headers:
        record_custom_parameter('Authorization', request.headers['Authorization'])
    if 'X-Coverage' in request.headers:
        record_custom_parameter('X-Coverage', request.headers['X-Coverage'])
    record_custom_parameter('version', VERSION)
    record_exception()
