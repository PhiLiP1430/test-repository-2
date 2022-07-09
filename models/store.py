from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    #every query or any command thru SQLAlchemy methods will be have this table named 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #list of Items from ItemModel
    #saying items have a relationship with ItemModel
    # if we have many store and many item
    # whenever we create a store model we are going to create an object for each item
    # that matches in store.id
    # we need to tell the db to not create each item an object by using
    # lazy='dynamic'

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()