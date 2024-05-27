from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime


db = SQLAlchemy()


class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    filepath = db.Column(db.String(255))
    uploaded_at = db.Column(DateTime, default=datetime.utcnow)


