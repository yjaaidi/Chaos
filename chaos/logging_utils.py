# Copyright (c) since 2001, Kisio Digital and/or its affiliates. All rights reserved.

import logging
from flask import request


class ChaosFilter(logging.Filter):

    def filter(self, record):
        try:
            record.request_id = request.id
        except RuntimeError:
            # if we are outside of a application context
            record.request_id = None
        return True
