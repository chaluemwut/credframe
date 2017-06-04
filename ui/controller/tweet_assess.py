# -*- coding: utf-8 -*-
import os, config, pickle
from flask import Blueprint, request
from webframe.py_webframework import ViewController, APIController
from helper.controller_helper import create_pagename
from pymongo import MongoClient

base_name = 'twassess'
url_name = '/' + base_name
twassess_blueprint = Blueprint(base_name, __name__)

client = MongoClient(host=config.db_host)
db = client['credframe']

class Index(ViewController):
    def process(self):
        self.page_name = create_pagename(base_name, 'index.html')
        return {}

twassess_blueprint.add_url_rule(url_name+'/', view_func=Index.as_view('index'))