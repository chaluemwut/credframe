# -*- coding: utf-8 -*-
import pickle, config
from config import db
from flask import Blueprint, request
from webframe.py_webframework import APIController

base_name = 'api'
url_name = '/' + base_name
api_blueprint = Blueprint(base_name, __name__)


class APIProcess(APIController):
    def process(self):
        model_id = request.args.get('model_id')
        data = request.args.get('data')
        x = [int(x) for x in data.split(',')]
        try:
            clf = pickle.load(open('{}/{}.obj'.format(config.model_model_filepath, model_id), 'rb'))
            y = clf.predict(x)
        except Exception as e:
            return {'error': 1, 'message': 'model error'}
        return {'error': 0, 'data': y[0]}


api_blueprint.add_url_rule(url_name + '/process', view_func=APIProcess.as_view('process'))
