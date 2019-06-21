#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import current_app
from werkzeug.local import LocalProxy

logger = LocalProxy(lambda: current_app.logger)

class AgentManagerException(Exception):

    """base exception"""

    msg_fmt = "An unknown exception occurred."
    code = 2999
    errors = {}

    def __init__(self, message=None, **kwargs):
        """
        :message: exception message

        """
        self.kwargs = kwargs
        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass
        else:
            self.code = int(self.kwargs['code'])

        if not message:
            try:
                self.message = self.msg_fmt % kwargs
            except Exception:
                logger.critical('Exception in string format operation.')
                self.message = self.msg_fmt

        self.message = str(message)

        self.errors = kwargs.get('errors', {})

        super(AgentManagerException, self).__init__(message)

    def __str__(self):
        """Support unicode str operation"""
        return self.message.encode('utf8')

    def format_message(self):
        """exception message."""
        return self.args[0]