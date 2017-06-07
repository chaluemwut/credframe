# -*- coding: utf-8 -*-
from flask import Blueprint, request
from webframe.py_webframework import ViewController

base_name = 'front'
url_name = '/' + base_name
front_blueprint = Blueprint(base_name, __name__)

class AboutUs(ViewController):
    def process(self):
        self.page_name = 'aboutus.html'
        return {}

class OurResearch(ViewController):
    def process(self):
        self.page_name = 'ourresearch.html'
        return {}

front_blueprint.add_url_rule(url_name + '/aboutus', view_func=AboutUs.as_view('aboutus'))
front_blueprint.add_url_rule(url_name+'/ourresearch', view_func=OurResearch.as_view('ourresearch'))
