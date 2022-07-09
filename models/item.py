from db import db

#db.Model will tell the SQLAlchemy that this classes will store in the db
class ItemModel(db.Model):
    #this part will tell SQLAlchemy how it must treat these items.
    __tablename__ = 'items'
    #every query or any command thru SQLAlchemy methods will be have this table named 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #A FOREIGN KEY is a field (or collection of fields) in one table, 
    # that refers to the PRIMARY KEY in another table. 
    # The table with the foreign key is called the child table, 
    # and the table with the primary key is called the referenced 
    # or parent table.
    store = db.relationship('StoreModel')
    #saying items have a relationship with StoreModel

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1
        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "SELECT * FROM items WHERE name=?"
        #result = cursor.execute(query, (name,))
        #row = result.fetchone()
        #conn.close()
        
        #if row:
            #return cls({row[0], row[1]})
        #    return cls(*row)

        #simplification
        #SQLAlchemy handles all these below, until close.
        #it finds data, a row, and it automatically converts that row to an object if it can..
        
        #returns the first row with the name
        
    #def insert(self):
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "INSERT INTO items VALUES (?, ?)"
        #cursor.execute(query, (self.name, self.price))

        #conn.commit()
        #conn.close()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    #def update(self):
    #    conn = sqlite3.connect('data.db')
    #    cursor = conn.cursor()

    #    query = "UPDATE items SET price=? WHERE name=?"
    #    cursor.execute(query, (self.price, self.name))

    #    conn.commit()
    #    conn.close()