# -*- coding: utf-8 -*-
from nlp.nlp import CRFWordSegment
from pymongo import MongoClient

client = MongoClient()
db = client['filterel']

def process():
    crf = CRFWordSegment()
    db_lst = db.filter_el.find()
    for data in db_lst[0:100]:
        line_arr = []
        try:
            if data['cred_value'] == 'yes':
                line_arr.append('1')
            else:
                line_arr.append('0')
            line_arr.append(data['likes'])
            line_arr.append(data['shares'])
            line_arr.append(data['comments'])
            line_arr.append(data['images'])
            line_arr.append(data['url'])
            line_arr.append(data['vdo'])
            line_arr.append(data['hashtag'])

            line_data = ','.join(line_arr)
            print(line_data)
        except Exception as e:
            print(str(e))
        # print(crf.crfpp(data['message']))

if __name__ == '__main__':
    process()