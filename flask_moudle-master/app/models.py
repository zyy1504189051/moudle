# coding: utf-8

import hashlib
from datetime import datetime

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.sql import func

from app import mysql_db


class CiAccount(mysql_db.Model):
    __tablename__ = 'ci_account'

    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    username = mysql_db.Column(mysql_db.String(32),
                               index=True, unique=True)
    password = mysql_db.Column(mysql_db.String(128),
                               nullable=False)
    vpn_username = mysql_db.Column(mysql_db.String(32), default='')
    vpn_password = mysql_db.Column(mysql_db.String(128), default='')
    ins_company = mysql_db.Column(mysql_db.String(16), default='')
    login_type = mysql_db.Column(mysql_db.Integer, default=0)
    department_code = mysql_db.Column(mysql_db.String(16), default='')
    department_name = mysql_db.Column(mysql_db.String(32), default='')
    seller_code = mysql_db.Column(mysql_db.String(16), default='')
    seller_name = mysql_db.Column(mysql_db.String(32), default='')
    area = mysql_db.Column(mysql_db.String(32), default='')
    proxy = mysql_db.Column(mysql_db.String(32), default='')
    is_bank = mysql_db.Column(mysql_db.Integer, default=0)
    cookies = mysql_db.Column(mysql_db.String(2000), default='')
    pre_url = mysql_db.Column(mysql_db.String(2000), default='')
    pre_verify = mysql_db.Column(mysql_db.Integer, default=-1)
    created = mysql_db.Column(mysql_db.DateTime,
                              default=func.now())
    updated = mysql_db.Column(mysql_db.TIMESTAMP,
                              default=func.now())


class CiAgent(mysql_db.Model):
    __tablename__ = 'ci_agent'

    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    partner_id = mysql_db.Column(mysql_db.Integer)
    agent_code = mysql_db.Column(mysql_db.String(32))
    agent_name = mysql_db.Column(mysql_db.String(32))
    created = mysql_db.Column(mysql_db.DateTime,
                              default=func.now())
    updated = mysql_db.Column(mysql_db.TIMESTAMP,
                              default=func.now())


class CiBranch(mysql_db.Model):
    __tablename__ = 'ci_branch'

    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    partner_id = mysql_db.Column(mysql_db.Integer)
    agent_id = mysql_db.Column(mysql_db.Integer)
    branch_code = mysql_db.Column(mysql_db.String(32))
    branch_name = mysql_db.Column(mysql_db.String(32))
    created = mysql_db.Column(mysql_db.DateTime,
                              default=func.now())
    updated = mysql_db.Column(mysql_db.TIMESTAMP,
                              default=func.now())


class CiPartner(mysql_db.Model):
    __tablename__ = 'ci_partner'

    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    account_id = mysql_db.Column(mysql_db.Integer)
    partner_code = mysql_db.Column(mysql_db.String(16))
    partner_name = mysql_db.Column(mysql_db.String(16))
    business_code = mysql_db.Column(mysql_db.String(16))
    business_detail_code = mysql_db.Column(mysql_db.String(16))
    channel_code = mysql_db.Column(mysql_db.String(16))
    channel_detail_code = mysql_db.Column(mysql_db.String(16))
    created = mysql_db.Column(mysql_db.DateTime,
                              default=func.now())
    updated = mysql_db.Column(mysql_db.TIMESTAMP,
                              default=func.now())


class CiProtocol(mysql_db.Model):
    __tablename__ = 'ci_protocol'

    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    partner_id = mysql_db.Column(mysql_db.Integer)
    agent_id = mysql_db.Column(mysql_db.Integer)
    branch_id = mysql_db.Column(mysql_db.Integer)
    protocol_code = mysql_db.Column(mysql_db.String(32))
    protocol_name = mysql_db.Column(mysql_db.String(32))
    protocol_sub_code = mysql_db.Column(mysql_db.String(32))
    product = mysql_db.Column(mysql_db.String(1000))
    created = mysql_db.Column(mysql_db.DateTime,
                              default=func.now())
    updated = mysql_db.Column(mysql_db.TIMESTAMP,
                              default=func.now())
