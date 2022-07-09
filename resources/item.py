import re
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank."
    )
    parser.add_argument('store_id',
        type=float,
        required=True,
        help="Items need store ID."
    )
    
    @jwt_required()
    def get(self, name):
        #item = next(filter(lambda x: x['name'] == name, items), None)
        ###items will be filtered
        ###filter doesn't return a single item, it returns a filtered object
        ###it returns all the items that match the item in the filter function
        ###next will return the first item that will match the item in the filter function
        ###next will break the program if there is no item left
        ###None, will return None if the item is not found.
        #return {'item': item}, 200 if item else 404
        item = ItemModel.find_by_name(name)
        if item:
            return item.json() # this will return item itself
            #the item returns an object not a dictionary just like before
        return {'message': 'Item not found.'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with the name '{}' already exists.".format(name)}, 400
        #elif StringCheck.check_string(name):
        #    return {'message': 'this field cannot be left blank or have special characters.'}
        data = Item.parser.parse_args()

        item = ItemModel(name, **data) # price, store_id from parse
        
        try:
            item.save_to_db()
            #insert just gives the object to the list "item"
        except:
            return {"message": "An error occured inserting the item."}, 500

        return item.json(), 201
    
    def delete(self, name):
        #global items
        #items from the items list outside this class.
        #items = list(filter(lambda x: x['name'] == name, items))
        
        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "DELETE FROM items WHERE name=?"
        #cursor.execute(query, (name,))

        #conn.commit()
        #conn.close()
        
        #return {'message': 'Item deleted.'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}

    def put(self, name):
        #create items or update existing items.

        data = Item.parser.parse_args()

        #item = next(filter(lambda x: x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name,data['price'])

        if item:
            item.price = data['price']
            #item = ItemModel(name, data['price'])
            #try:
            #    updated_item.save_to_db()
            #except:
            #    return {'message':'error.'}, 500
        else:
            item = ItemModel(name, **data) # price, store_id from parse
            #try:
             #   updated_item.update()
             #   #inserts the item to the dictionary
            #except:
            #    return {'message': 'An error occured updating the item.'}, 500
        item.save_to_db()

        return item.json()
    

class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        #return {'items': [x.json() for x in ItemModel.query.all()]}

        #ItemModel.query.all()
        #ItemModel - will get the tablename from the ItemModel class
        #.query.all() - will perform the query select all
        #list() will convert the items to list objects
        #map() - allows you to process and transform all the items 
        # in an iterable without using an explicit for loop, a technique 
        # commonly known as mapping. map() is useful when you need to apply 
        # a transformation function to each item in an iterable 
        # and transform them into a new iterable.
        #lambda -  lambda function can take any number of arguments, 
        # but can only have one expression.

        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "SELECT * FROM items"
        #qResult = cursor.execute(query)

        #items = []
        #for row in qResult:
        #    items.append({'name': row[0], 'price': row[1]})

        #conn.close

        #return {'items': items}


class StringCheck:
    def check_string(name):
        if re.findall('<' or '>', name) == None:
            return None
        else:
            return True