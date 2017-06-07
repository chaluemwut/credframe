from flask import Flask
from flask.templating import render_template
from controller.cred_frame import frame_blueprint
from controller.fb_assess import fbassess_blueprint
from controller.tweet_assess import twassess_blueprint
from controller.cred_api import api_blueprint
from controller.fb_training_collection import fbcollect_blueprint
from controller.front_end import front_blueprint

app = Flask(__name__)
app.register_blueprint(frame_blueprint)
app.register_blueprint(fbassess_blueprint)
app.register_blueprint(twassess_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(fbcollect_blueprint)
app.register_blueprint(front_blueprint)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT Rv]]jkojkiyd'

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)