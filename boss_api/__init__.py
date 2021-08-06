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


def create_app(comfig_name):
    app = Flask(__name__)

    app.config.from_object(config[comfig_name])
    config[comfig_name].init_app(app)

    return app
