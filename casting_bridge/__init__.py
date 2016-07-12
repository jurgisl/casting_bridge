import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.admin import Admin

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx','mov','mp4','mp3','wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/uploads/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../cb.db'
app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
app.config['USER'] = 'demo'
app.config['PIN'] = 'demo'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
admin = Admin(app)

app.secret_key = 'some_random_key'

from casting_bridge.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()



