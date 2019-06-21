#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import current_app
from werkzeug.local import LocalProxy

from huiyou_util import encryption

logger = LocalProxy(lambda: current_app.logger)

def fields_encrypt(fields):
    for f, v in fields.items():
        if isinstance(v, dict):
            # 递归加密
            fields[f] = fields_encrypt(v)
            continue
        if f in current_app.config['ENCRYPTION_SECRET_FIELDS']:
            fields[f] = encryption.encrypt(
                source=v,
                key=current_app.config['ENCRYPTION_SECRET_KEY'])
    return fields

def fields_decrypt(fields):
    for f, v in fields.items():
        if isinstance(v, dict):
            # 递归解密
            fields[f] = fields_decrypt(v)
            continue
        if f in current_app.config['ENCRYPTION_SECRET_FIELDS']:
            fields[f] = encryption.decrypt(
                crypt=v,
                key=current_app.config['ENCRYPTION_SECRET_KEY'])
    return fields
