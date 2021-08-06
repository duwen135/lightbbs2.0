#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: __init__.py.py
# @Author: duwen
# @E-mail: duwen135@163.com
# @Site: 
# @Time: 8月 06, 2021
# ---

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.boss_api import boss as boss_api

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    # 注册配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 注册蓝图
    app.register_blueprint(boss_api, url_prefix='/boss_api')
    # 注册插件
    db.init_app(app)
    migrate.init_app(app)

    return app
