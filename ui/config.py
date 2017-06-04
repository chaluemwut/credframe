base_filepath = '/data/cred_frame_data'
model_model_filepath = base_filepath+'/model'

# API
api_url = 'https://fbcredibility.com/api/process'

import os
from pymongo import MongoClient
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
# client = MongoClient(host=db_host)
db = client['credframe']