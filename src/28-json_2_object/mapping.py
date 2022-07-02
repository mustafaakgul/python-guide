# class User(object):
#     def __init__(self, name, username):
#         self.name = name
#         self.username = username
#
# import json
# j = json.loads(your_json)
# u = User(**j)

import json
class Address(object):
    def __init__(self, street: str, number):
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1}".format(self.street, self.number)

class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = Address(**address)

    def __str__(self):
        return "{0} ,{1}".format(self.name, self.address)

if __name__ == '__main__':
    js = '''{"name":"Cristian", "address":{"street":"Sesame","number":122}}'''
    j = json.loads(js)
    print(j)
    u = User(**j)
    print(u)

    # ***
    labeled_images = json.loads(json_str2, object_hook=ImageLabelCollection.from_json)
    label_decoded = json.loads(json_str, object_hook=Label.from_json)

