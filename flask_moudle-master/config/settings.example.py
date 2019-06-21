#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# System
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
SSL_DISABLE = True
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')

# Encryption
# 加密KEY，该设置一旦在线上运行，则不允许更改，否则会造成无法解密
ENCRYPTION_SECRET_KEY = ''
# 需要加密的字段名称
ENCRYPTION_SECRET_FIELDS = ['password', 'vpn_password']

# MySQL
SQLALCHEMY_DATABASE_URI = (os.environ.get('ONLINE_DATABASE_URL') or
                           'mysql+mysqlconnector://super_test:rt12tst99hy@118.190.1.72:3306/car_ins_agent_account')
SQLALCHEMY_ECHO = True
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # autocommit

MYSQL_DB_SESSION_OPTIONS = {
    "autoflush": True,
    "autocommit": False,
    "expire_on_commit": False  # 要与autocommit取值一致，否则autocommit行为不正确
}

# MongoDB

# MONGODB_SETTINGS = {
#     'db': 'InsSearch',
#     'host': '118.190.25.4',
#     'port': 27017
# }

# Redis
# REDIS_SETTINGS = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_HOST': '118.190.94.125',
#     'CACHE_REDIS_PORT': 57619,
#     'CACHE_REDIS_DB': '3',
#     'CACHE_REDIS_PASSWORD': 'food5205NFIGcocc15ed'
# }



LOGGER_NAME = 'agent_mgr'  # 名称要与logging配置文件（log.cfg）一致
LOGGER_HANDLER_POLICY = 'always'


