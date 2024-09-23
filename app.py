import os
from flask import Flask
from blueprint.catpics.catpics import catpics

app = Flask(__name__)

app.secret_key = os.environ['FLASK_APPLICATION_SECRET_KEY']

app.register_blueprint(catpics, url_prefix='/catpics')

if '__main__' == __name__:
    app.run(host='0.0.0.0')
