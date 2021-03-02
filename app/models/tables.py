from app import db
import uuid

class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(64))
    properties = db.relationship('Property', backref='table', lazy='dynamic')


    def __repr__(self):
        return '<Table \'%s\'>' % self.name
