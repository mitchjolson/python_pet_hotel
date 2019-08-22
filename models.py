from app import db

class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    name = db.Column(db.String())
    breed = db.Column(db.String())
    color = db.Column(db.String())
    checked_in = db.Column(db.String())
    owner_name = db.Column(db.String())

    def __init__(self, owner_id, name, breed, color, checked_in, owner_name):
        self.name = name
        self.owner_id = owner_id
        self.breed = breed
        self.color = color
        self.checked_in = checked_in
        self.owner_name = owner_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'owner_id': self.owner_id,
            'name': self.name,
            'breed': self.breed,
            'color': self.color,
            'checked_in': self.checked_in,
            'owner_name': self.owner_name
        }




class Owner(db.Model):
        __tablename__ = 'owner'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String())

        def __init__(self, name):
            self.name = name

        def __repr__(self):    
            return '<id {}>'.format(self.id)

        def serialize(self):
            return {
            'id': self.id, 
            'name': self.name,
        }
    
