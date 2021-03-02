from app import db
import uuid

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    price = db.Column(db.Integer)
    rent = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'))


    def __repr__(self):
        return '<Property \'%s\'>' % self.id
