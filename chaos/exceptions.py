# Copyright (c) since 2001, Kisio Digital and/or its affiliates. All rights reserved.


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
