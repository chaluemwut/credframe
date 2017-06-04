# -*- coding: utf-8 -*-
import config, pickle
from flask import Blueprint, request
from webframe.py_webframework import ViewController
from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
from helper.controller_helper import create_pagename
from config import db

app_name = '/frame'
frame_blueprint = Blueprint('frame', __name__)

class Index(ViewController):
    def process(self):
        self.page_name = 'frame/index.html'
        return {}

class ModelList(ViewController):

    def create_url(self, model_id, simple_data):
        str = '{}?model_id={}&data={}'.format(config.api_url, model_id, simple_data)
        return str

    def process(self):
        self.page_name = 'frame/list.html'
        lst = db.model_data.find()
        data_list = []
        for m in lst:
            data = {}
            data['id'] = str(m['_id'])
            data['name'] = m['name']
            data['field'] = m['field']
            data['url'] = self.create_url(str(m['_id']), m['simple_data'])
            data['description'] = m['description']
            data_list.append(data)
        return {'data_list': data_list}

class UploadModelIndex(ViewController):
    def process(self):
        self.page_name = 'frame/upload.html'
        return {}

class UploadModelProcess(ViewController):
    def process(self):
        self.page_name = 'frame.list_model'
        self.is_controller_page = True

        if request.method == 'POST':
            data = {}
            if 'file' not in request.files:
                pass

            model_name = request.form['model_name']
            model_description = request.form['description']
            data['name'] = model_name
            data['description'] = model_description
            file = request.files['file']
            lines = file.readlines()
            header = lines[0]
            arr_field = header.decode('utf-8').replace('\n', '').split(',')
            str_field = ','.join(arr_field[1:])
            data['field'] = str_field
            x = []
            y = []
            for l in lines[1:]:
                line_data = l.decode('utf-8').replace('\n', '')
                training_data = line_data.split(',')
                y.append(training_data[0])
                x.append(training_data[1:])

            data['simple_data'] = ','.join(x[0])
            row_id = db.model_data.insert(data)

            clf = RandomForestClassifier()
            clf = clf.fit(x, y)
            pickle.dump(clf, open('{}/{}.obj'.format(config.model_model_filepath, str(row_id)), 'wb'))
        return {}


class DetailModel(ViewController):
    def process(self):
        model_id = request.args.get('model_id')
        model_obj = db.model_data.find({'_id':model_id})
        self.page_name = create_pagename(app_name, 'detail.html')
        return {}

frame_blueprint.add_url_rule(app_name + '/', view_func=Index.as_view('index'))
frame_blueprint.add_url_rule(app_name + '/list', view_func=ModelList.as_view('list_model'))
frame_blueprint.add_url_rule(app_name + '/upload/', view_func=UploadModelIndex.as_view('upload'))
frame_blueprint.add_url_rule(app_name + '/upload/process/', view_func=UploadModelProcess.as_view('upload_process'),
                             methods=['post'])
frame_blueprint.add_url_rule(app_name+'/detail', view_func=DetailModel.as_view('detail'))
