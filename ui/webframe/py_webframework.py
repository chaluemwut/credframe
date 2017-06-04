# -*- coding: utf-8 -*-
import json
from flask import Response, request, redirect, url_for
from flask.views import View
from flask import render_template


class BaseView(View):
    controller_debug = False

    def __init__(self):
        pass

    def get_parameters(self, params):
        ret = {}
        for p in params:
            ret[p] = request.args.get(p)
        return ret


class APIController(BaseView):
    def process(self):
        raise NotImplementedError()

    def dispatch_request(self):
        data = None
        map_result = {}
        try:
            map_result['status'] = 0
            map_result['description'] = 'OK Request'
            data = self.process()
            if data != None and data['error'] == 0:
                map_result['data'] = data['data']
            else:
                map_result['data'] = None
                map_result['status'] = data['error']
                map_result['description'] = data['message']
        except Exception as e:
            print(e)
            map_result['status'] = 1
            map_result['description'] = 'Request error'
        from bson import json_util
        json_result = json.dumps(map_result, default=json_util.default)

        data = None
        map_result = {}

        return Response(json_result, mimetype='application/json')


class ViewController(View):
    is_controller_page = False
    page_name = None

    def process(self):
        raise NotImplementedError()

    def dispatch_request(self):
        try:
            result = self.process()
            if self.is_controller_page:
                return redirect(url_for(self.page_name))
            else:
                return render_template(self.page_name, **result)
        except Exception as e:
            print(e)
