from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'phil'
api = Api(app)

@app.before_first_request #flask decorator
#this will run first over all the request

def create_tables():
    db.create_all()

#SQLAlchemy creates the table for us using the code above.
#the above code looks for the resource to find the table it needs to create.
#Ex. This will look at the store resource and look for the Store class which
# has the __tablename__ = 'store'
#then it will create that table. and in that file, there is a specified column for 
# the specific table it needs to create

jwt = JWT(app, authenticate, identity)
#JWT will create a new endpoint called /auth
#when we call /auth we send it a username and password
#..then sends it over to the authenticate function in security.py
#Output Codes
#404 - Not Found
#200 - Ok
#201 - Created
#202 - Accepted
#500 - Internal Server Error

api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>') #http://127.0.0:5000/item/<string:name>

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    
    #debug=True is a Flask feature to help us debug
    #if we run the app.py, python assigns a special name to the file and the namin is always '__main__'

#When a Python interpreter reads a Python file, 
# it first sets a few special variables. 
# Then it executes the code from the file.
#One of those variables is called __name__.
#So when the interpreter runs a module, 
# the __name__ variable will be set as  __main__ 
# if the module that is being run is the main program.
#basta kapag nirun mo itong file na ito, magiging '__main__' ang value ng special
# variable niya. kapag hindi, yung file name mismo niya ang magiging value non.