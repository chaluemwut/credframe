# -*- coding: utf-8 -*-
import pickle, config
from config import db
from flask import Blueprint, request
from webframe.py_webframework import APIController

base_name = 'fbcollect'
url_name = '/' + base_name
fbcollect_blueprint = Blueprint(base_name, __name__)


class FBCollection(APIController):
    ret_data = {'error': 0}

    def process(self):
        db_data = {}
        return_id = request.args.get('return_id')
        cred_value = request.args.get('cred_value')
        likes = request.args.get('likes')
        comments = request.args.get('comments')
        shares = request.args.get('shares')
        hash_tag = request.args.get('hash_tag')
        image = request.args.get('images')
        vdo = request.args.get('vdo')
        poster_id = request.args.get('poster_id')
        message = request.args.get('message')

        db_data['cred_value'] = cred_value
        db_data['likes'] = likes
        db_data['shares'] = shares
        db_data['comments'] = comments
        db_data['hash_tag'] = hash_tag
        db_data['image'] = image
        db_data['vdo'] = vdo
        db_data['hash_tag'] = hash_tag
        db_data['poster_id'] = poster_id
        db_data['message'] = message
        db.fb_training_collect.insert(db_data)
        self.ret_data['data'] = {'return_id': return_id}
        return self.ret_data


fbcollect_blueprint.add_url_rule(url_name + '/process', view_func=FBCollection.as_view('process'))
