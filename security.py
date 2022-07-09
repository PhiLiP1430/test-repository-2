
from hmac import compare_digest
from resources.user import UserModel

#in memory table of users
#users = [
#    User(1, 'bob', 'asdf')
#]

#these mappings are used for us to not iterate over every users everytime.
#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}

#this will authenticate the user if the user is in the database.
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    #user = username_mapping.get(username, None)
    if user and compare_digest(user.password, password):
        return user

#from JWT, payLoad, contents of JWT.
#retrive a specific user using the specific "payLoad"
def identity(payLoad):
    user_id = payLoad['identity']
    return UserModel.find_by_id(user_id)