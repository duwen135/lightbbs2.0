#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: config.py
# @Author: duwen
# @E-mail: duwen135@163.com
# @Site: 
# @Time: 8月 06, 2021
# ---
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:////' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ###flask-session
    # SESSION_TYPE = 'null'
    # SESSION_KEY_PREFIX = "session:"
    # ########如果设置为True的话，session的生命为 permanent_session_lifetime 秒（默认是31天）
    # ########如果设置为False的话，那么当用户关闭浏览器时，session便被删除了。permanent_session_lifetime也会生效
    # SESSION_PERMANENT = False
    # PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 31

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
