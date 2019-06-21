#!/usr/bin/env python
# -*- coding: utf-8 -*-

from api_1_0.views import *


urls = (
    (Index, '/'),
    (AccountAdd, '/api/v1/account/add'),
    (AccountDetail, '/api/v1/account/detail'),
    (AccountModify, '/api/v1/account/modify'),
    (AccountLogin, '/api/v1/account/login'),
)
