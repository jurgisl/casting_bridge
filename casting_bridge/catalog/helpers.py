from flask import request
from werkzeug import secure_filename
from casting_bridge import db, app, ALLOWED_EXTENSIONS
from casting_bridge.catalog.models import Document
import os
from datetime import datetime
import pytz

def allowed_file(filename):
    return '.' in filename and \
            filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def file_upload(type, name, id):
    file = request.files[name]
    filename = ''
    if file and allowed_file(file.filename):
        filename = str(id) + "_" + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        add_document = Document(datetime.now(pytz.timezone("Europe/Riga")), id, type, filename)
        db.session.add(add_document)
