class User(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username

import json
def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'User':
        return User(obj['name'], obj['username'])
    return obj

json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}',
           object_hook=object_decoder)

print(type(User))  # -> <type 'type'>

user = json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}')
print(user['name'])
print(user['username'])