#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests
import base64
from flask import jsonify
from flask import request
from flask_restful import Resource
from flask_restful import reqparse

from app.models import *
from app import errors
from app import utils
from app import OSLO_CONF
from app.exceptions import AgentManagerException
from flask import current_app
from werkzeug.local import LocalProxy

from huiyou_util import encryption

from car_ins_client.taipy.taipy_client import TaipyClient
from car_ins_client.taipy_wx.taipy_wx_client import TaipyWxClient
from car_ins_client.exception import InsuranceException

logger = LocalProxy(lambda: current_app.logger)

parser = reqparse.RequestParser()


class BaseApi(Resource):
    def __init__(self):
        super(BaseApi, self).__init__()
        self.request_token = ''

    def post(self):
        try:

            result = self._post()
            return self._success(data=result), 200
        except AgentManagerException as ame:
            return self._error(code=ame.code,
                               message=ame.message,
                               ext_errors=ame.errors), 200
        except InsuranceException as ie:
            return self._error(code=ie.code,
                               message=ie.message), 200
        except Exception as e:
            logger.exception(e)
            return self._error(code=AgentManagerException.code,
                               message=e.message), 200

    def _post(self):
        raise NotImplementedError

    def get(self, id):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def _error(self, code, message, ext_errors={}):
        return {
            "request_token": self.request_token,
            "status": "fail",
            "error": {
                "code": code,
                "message": message,
                "errors": json.dumps(ext_errors)
            }
        }

    def _success(self, data):
        return {
            "request_token": self.request_token,
            "status": "success",
            "data": data
        }


class Index(BaseApi):
    def get(self):
        args = parser.parse_args()
        return args, 200

    def _post(self):
        return ''


class AccountAdd(BaseApi):
    """
    添加账号
    """

    def _post(self):
        parser.add_argument('request_token', type=str, required=True, help='请求唯一标识')
        parser.add_argument('account', type=dict)
        args = parser.parse_args()
        self.request_token = args.get('request_token',
                                      self.request_token)
        logger.debug(args)
        fields = args.get('account', {})
        if not fields:
            errors.PARAMS_ERROR.exception()

        fields = utils.fields_encrypt(fields=fields)

        logger.debug(fields)

        account = CiAccount(**fields)
        mysql_db.session.add(account)
        mysql_db.session.commit()
        return {'account_id': account.id}


class AccountDetail(BaseApi):
    """
    账号详情
    """

    def _post(self):
        parser.add_argument('request_token', type=str, required=True, help='请求唯一标识')
        parser.add_argument('account', type=dict)
        parser.add_argument('need_password', type=bool)
        args = parser.parse_args()
        self.request_token = args.get('request_token',
                                      self.request_token)

        need_password = args.get('need_password', False)
        logger.debug(need_password)
        logger.debug(type(need_password))
        account_id = args['account']['account_id']
        account = CiAccount.query.get(account_id)

        if account:
            result = {
                "account_id": account.id,
                "username": account.username,
                "password": '',
                "vpn_username": account.vpn_username,
                "vpn_password": '',
                "ins_company": account.ins_company,
                "login_type": account.login_type,
                "cookies": "",
                "area": account.area,
                "is_bank": account.is_bank,
                "pre_url": account.pre_url,
                "pre_verify": account.pre_verify,
                "proxy": account.proxy,
                "host": ""
            }

            if account.cookies:
                if account.ins_company == 'taipy':
                    result['cookies'] = account.cookies
                if account.ins_company == 'taipy_wx':
                    appends = json.loads(base64.b64decode(account.cookies))
                    logger.info(appends['cookies'])
                    result['agent'] = appends['agent']
                    result['channel'] = appends['channel']
                    result['cookies'] = base64.b64encode(json.dumps(appends['cookies']))
            if need_password:
                result["password"] = account.password
                result["vpn_password"] = account.vpn_password
                result = utils.fields_decrypt(fields=result)

            return result

        else:
            # 使用 exception 方法 直接抛出异常
            errors.NOT_FOUND_RECORD.exception()


class AccountModify(BaseApi):
    """
    修改账号
    """
    def _post(self):
        parser.add_argument('request_token', type=str, required=True, help='请求唯一标识')
        parser.add_argument('account', type=dict)
        args = parser.parse_args()
        self.request_token = args.get('request_token',
                                      self.request_token)
        logger.debug(args)
        if not args.get('account', None):
            errors.PARAMS_ERROR.exception()

        account_id = args['account']['account_id']
        account = CiAccount.query.get(account_id)

        if not account:
            errors.NOT_FOUND_RECORD.exception()

        fields = args['account'].copy()
        if 'account_id' in fields:
            del fields['account_id']

        fields = utils.fields_encrypt(fields=fields)

        CiAccount.query.filter_by(id=account.id).update(fields)
        mysql_db.session.commit()
        return {'account_id': account.id}


class AccountLogin(BaseApi):
    """
    账号登录
    """

    def _post(self):
        parser.add_argument('request_token', type=str, required=True, help='请求唯一标识')
        parser.add_argument('account', type=dict)
        args = parser.parse_args()
        self.request_token = args.get('request_token',
                                      self.request_token)

        account_id = args['account']['account_id']
        account = CiAccount.query.get(account_id)

        if account:
            if account.ins_company == 'taipy':
                return self._taipy_login(account=account)
            if account.ins_company == 'taipy_wx':
                return self._taipy_wx_login(account=account)


        else:
            # 使用 exception 方法 直接抛出异常
            errors.NOT_FOUND_RECORD.exception()

    def _taipy_login(self, account):
        api = TaipyClient(
            conf=OSLO_CONF,
            username=account.username,
            password=encryption.decrypt(
                crypt=account.password,
                key=current_app.config['ENCRYPTION_SECRET_KEY'])
        )

        status = api.login()
        cookies = base64.b64encode(
            json.dumps(
                requests.utils.dict_from_cookiejar(
                    api.session.cookies)))

        logger.debug(api.cookies)
        cookies = base64.b64encode(
            json.dumps(api.cookies))

        logger.debug(status)
        if status:
            CiAccount.query.filter_by(id=account.id).update({'cookies': cookies})
            mysql_db.session.commit()

        result = {
            "account_id": account.id,
            "agent": "",
            "channel": "",
            "cookies": cookies
        }
        return result

    def _taipy_wx_login(self, account):
        partner = CiPartner.query.filter_by(account_id=account.id).first()
        api = TaipyWxClient(
            conf=OSLO_CONF,
            username=account.username,
            password=encryption.decrypt(
                crypt=account.password,
                key=current_app.config['ENCRYPTION_SECRET_KEY']),
            unitcode=partner.partner_code
        )

        login_data = api.login()

        result = {
            "account_id": account.id,
            "agent": "",
            "channel": "",
            "cookies": ""
        }

        logger.debug(login_data)
        if login_data.get('status') and login_data.get('data'):
            cookies = base64.b64encode(
                json.dumps(login_data['data']))
            CiAccount.query.filter_by(id=account.id).update(
                {'cookies': cookies})
            mysql_db.session.commit()
            result['agent'] = login_data['data'].get('agent', '')
            result['channel'] = login_data['data'].get('channel', '')
            result['cookies'] = base64.b64encode(
                json.dumps(login_data['data']['cookies']))

        return result
