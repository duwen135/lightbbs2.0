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
from flask import Blueprint

boss = Blueprint('boss_api', __name__)

from api.boss_api import user
