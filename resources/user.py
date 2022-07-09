from flask_restful import Resource, reqparse
from models.user import UserModel
#import sqlite3
#by having sqlite3, this file can now interact with sql

#the User class should not be the same as the class for registering a new user.
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required=True,
                        help="This field cannot be blank."
    )
    parser.add_argument('password',
                        type = str,
                        required=True,
                        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'username already exists.'}, 400
        #if username exist, program will end here.

        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        #conn = sqlite3.connect('data.db')
        #cursor = conn.cursor()

        #query = "INSERT INTO users VALUES (NULL, ?, ?)"
        #cursor.execute(query, (data['username'], data['password'],))

        #conn.commit()
        #conn.close()

        return {"message": "User created successfully."}, 201