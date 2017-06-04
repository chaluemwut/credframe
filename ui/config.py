base_filepath = '/data/cred_frame_data'
model_model_filepath = base_filepath+'/model'

# API
api_url = 'http://fbcredibility.com/api/process'

# database
db_host='localhost'

from pymongo import MongoClient
# client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
client = MongoClient(host=db_host)
db = client['credframe']