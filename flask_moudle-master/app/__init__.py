#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import logging

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from logging.config import fileConfig
from oslo_config import cfg

from config import settings

import car_ins_client

OSLO_CONF = cfg.CONF
car_ins_client.register_opts(OSLO_CONF)

fileConfig(fname='%s/config/log.cfg' % settings.BASE_DIR)

mysql_db = SQLAlchemy(
    session_options=settings.MYSQL_DB_SESSION_OPTIONS)
api = None


def create_app(config_name):
    app = Flask(__name__,
                template_folder=settings.TEMPLATE_PATH,
                static_folder=settings.STATIC_PATH)
    cfg_filename = '%s/config/%s.py' % (settings.BASE_DIR, config_name)
    app.config.from_pyfile(filename=cfg_filename)
    app._logger = logging.getLogger(app.logger_name)

    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    # or using lazy instantiation

    mysql_db.init_app(app)

    # from app.urls import api as resful
    # 注意，init_app方式无法执行，报报 404 错误
    api = Api(app)

    # 注意 init 顺序
    import urls
    for u in urls.urls:
        api.add_resource(*u)

    # app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
