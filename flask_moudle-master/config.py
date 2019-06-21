#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Config(object):
    DEBUG = False

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    MONGODB_SETTINGS = {
        'db': 'InsSearch',
        'host': '118.190.25.4',
        'port': 27017
    }

    REDIS_SETTINGS = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '118.190.94.125',
        'CACHE_REDIS_PORT': 57619,
        'CACHE_REDIS_DB': '3',
        'CACHE_REDIS_PASSWORD': 'food5205NFIGcocc15ed'
    }

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')

    LOGGING = {
        'version': 1,
        'loggers': {
            'flask': {
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class PrdConfig(Config):
    # DEBUG = False
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
    MONGODB_SETTINGS = {
            'db': os.environ.get('DB_NAME') or 'InsSearch',
            'host': os.environ.get('MONGO_HOST') or 'localhost',
            'port': 12345
        }
    REDIS_SETTINGS = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '118.190.94.125',
        'CACHE_REDIS_PORT': 57619,
        'CACHE_REDIS_DB': '3',
        'CACHE_REDIS_PASSWORD': 'food5205NFIGcocc15ed'
    }


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'InsSearch',
        'host': '118.190.25.4',
        'port': 27017
    }
    WTF_CSRF_ENABLED = False


config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'default': TestingConfig,
}
