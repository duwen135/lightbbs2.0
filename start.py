#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: start.py
# @Author: duwen
# @E-mail: duwen135@163.com
# @Site: 
# @Time: 8月 06, 2021
# ---
import os
from boss_api import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")

if __name__ == "__main__":
    app.run()