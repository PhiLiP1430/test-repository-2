from db import db

#db.Model will tell the SQLAlchemy that this classes will store in the db
class UserModel(db.Model): #helper
    __tablename__ = 'users'
    #every query or any command thru SQLAlchemy methods will be have this table named 'users'

    #this are the items that SQLAlchemy will look for.
    #this must match the columns for this to be saved into the db.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        #SELECT * FROM users WHERE username=? LIMIT 1

        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "SELECT * FROM users WHERE username=?"
        #result = cursor.execute(query, (username,)) #may coma kasi tuple
        #row = result.fetchone()
        #fetchone() will get the first row that will match the username

        #if row:
            #user = cls(row[0], row[1], row[2])
        #    user = cls(*row)
        #else:
        #    user = None

        #conn.close()
        #return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        #SELECT * FROM users WHERE id=? LIMIT 1

        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "SELECT * FROM users WHERE id=?"
        #result = cursor.execute(query, (_id,)) #may coma kasi tuple
        #row = result.fetchone()
        #fetchone() will get the first row that will match the username

        #if row:
            #user = cls(row[0], row[1], row[2])
        #    user = cls(*row)
        #else:
        #    user = None

        #conn.close()
        #return user
