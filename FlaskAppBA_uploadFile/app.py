import os
from flask import Flask
from UploadFileBlueprint.db_models import db
from UploadFileBlueprint.uploadFileBlueprint import uploadFile_BP
from flask_wtf.csrf import CSRFProtect

basedir = os.path.abspath(os.path.dirname(__file__))

# Anwendung erstellen
app = Flask(__name__)

# Konfigurationen für die Anwendung
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blueprint_fileupload.db')

# Datenbank auf die Applikation registrieren
db.init_app(app)

# Anwendung vor übergreifender Anfragenfälschung sichern
csrf = CSRFProtect(app)

# Datenbank modelle initialisieren
with app.app_context():
    db.create_all()

# Blueprint in Hauptanwendung registrieren
app.register_blueprint(uploadFile_BP)

# -- von Flask selber generiert --
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True) # debug true angepasst
