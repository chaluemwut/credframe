# -*- coding: utf-8 -*-
import os, config, pickle
from flask import Blueprint, request
from webframe.py_webframework import ViewController, APIController
from pymongo import MongoClient
from config import db

base_name = 'fbassess'
url_name = '/' + base_name
fbassess_blueprint = Blueprint(base_name, __name__)

base_model = 'base.dump'


def create_pagename(page_name):
    return '{}/{}'.format(base_name, page_name)


class Index(ViewController):
    def process(self):
        self.page_name = create_pagename('index.html')
        return {}


class FBAssess(APIController):
    def process(self):
        likes = request.args.get('like_count')
        shares = request.args.get('share_count')
        comments = request.args.get('comment_count')
        message = request.args.get('message')
        return {'error': 0, 'data': {'cred': 'Trustworthiness'}}


class AssessProcess(ViewController):
    def process(self):
        likes = request.args.get('likes')
        shares = request.args.get('shares')
        comments = request.args.get('comments')
        # x = [likes, shares, comments]
        # clf = pickle.load(open(''.format(config.model_model_filepath), 'rb'))
        # y = clf.fit(x)
        self.page_name = create_pagename('result.html')
        return {}


fbassess_blueprint.add_url_rule(url_name + '/', view_func=Index.as_view('index'))
fbassess_blueprint.add_url_rule(url_name + '/process', view_func=AssessProcess.as_view('process'))
fbassess_blueprint.add_url_rule(url_name + '/assess', view_func=FBAssess.as_view('assessment'))
