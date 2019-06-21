#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.exceptions import AgentManagerException

class ErrorItem(object):
    _code = 0
    _message = ''

    def __init__(self, code, message):
        self._code = int(code)
        self._message = str(message)

    def __int__(self):
        return self._code

    def __str__(self):
        return self._message

    def exception(self):
        raise AgentManagerException(
            code=int(self),
            message=str(self))


PARAMS_ERROR = ErrorItem(2001, '缺少必要参数')
NOT_FOUND_RECORD = ErrorItem(2002, '记录未找到')
