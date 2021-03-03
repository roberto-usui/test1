import uuid

from app import db
import random

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(64))
    play_pattern = db.Column(db.String(64))
    total_sum = db.Column(db.Integer)
    current_position = db.Column(db.Integer)
    properties = db.relationship('Property', backref='owner', lazy='dynamic')

    @staticmethod
    def insert_players():
        db.session.add(Player(name='Impulsive', play_pattern='impulsive', current_position=0, total_sum=300))
        db.session.add(Player(name='Cautious', play_pattern='cautious', current_position=0, total_sum=300))
        db.session.add(Player(name='Rigorous', play_pattern='rigorous', current_position=0, total_sum=300))
        db.session.add(Player(name='Random', play_pattern='random', current_position=0, total_sum=300))
        db.session.commit()

    def will_buy(self, property_price: int, property_rent: int) -> bool:
        if self.play_pattern == 'impulsive' and property_price < self.total_sum:
            return True
        elif self.play_pattern == 'rigorous' and property_price < self.total_sum and property_rent > 50:
            return True
        elif  self.play_pattern == 'cautious' and property_price < self.total_sum and (self.total_sum - property_price) > 80:
            return True
        elif  self.play_pattern == 'random' and property_price < self.total_sum and random.random() <= 0.5:
            return True
        else:
            return False


    def __repr__(self):
        return f'Person(name={self.name}, current_position={self.current_position}, total_sum={self.total_sum})'
