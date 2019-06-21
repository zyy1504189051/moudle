#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(
    os.path.abspath(__file__ + "/../../.."))

import json
import base64
import logging
import datetime
from app import mysql_db
from app.models import CiAccount
from app.models import CiPartner
from flask import current_app
from flask_script import Command, Option

import time

from app import OSLO_CONF
from car_ins_client.taipy.taipy_client import TaipyClient
from car_ins_client.taipy_wx.taipy_wx_client import TaipyWxClient
from huiyou_util import encryption

# from app.models import Order, Ticket


from werkzeug.local import LocalProxy
logger = LocalProxy(lambda: current_app.logger)

class LoginKeeper(Command):
    def __init__(self):
        super(LoginKeeper, self).__init__()

    def run(self):

        while True:
            try:
                rows = mysql_db.session.query(CiAccount).filter(CiAccount.cookies != '')
                for account in rows:
                    api = None
                    if account.ins_company == 'taipy':
                        cookies = json.loads(base64.b64decode(account.cookies))
                        api = TaipyClient(
                            conf=OSLO_CONF,
                            username=account.username,
                            password=encryption.decrypt(
                                crypt=account.password,
                                key=current_app.config['ENCRYPTION_SECRET_KEY']),
                            cookies=cookies
                        )
                    if account.ins_company == 'taipy_wx':
                        partner = CiPartner.query.filter_by(account_id=account.id).first()
                        cookies = json.loads(base64.b64decode(account.cookies)).get('cookies', None)
                        api = TaipyWxClient(
                            conf=OSLO_CONF,
                            username=account.username,
                            password=encryption.decrypt(
                                crypt=account.password,
                                key=current_app.config['ENCRYPTION_SECRET_KEY']),
                            cookies=cookies,
                            unitcode=partner.partner_code
                        )
                    if api and not api.is_login():
                        logger.info('clear cookies')
                        mysql_db.session.query(CiAccount).filter_by(id=account.id).update(
                            {'cookies': ''})
                    else:
                        logger.info('keep success')

            except Exception as e:
                logger.exception(e)
            finally:
                mysql_db.session.commit()
                time.sleep(3)


if __name__ == '__main__':
    LoginKeeper().run()
