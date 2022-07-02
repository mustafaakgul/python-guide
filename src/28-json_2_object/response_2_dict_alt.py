import json

class obj(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

def dict2obj(d):
    return json.loads(json.dumps(d), object_hook=obj)

d = {'a': 1, 'b': {'c': 2}, 'd': ['hi', {'foo': 'bar'}]}
object = dict2obj(d)
print(object.b.c)