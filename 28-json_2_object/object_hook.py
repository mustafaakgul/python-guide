import json
from collections import namedtuple
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


def customDecoder(geekDict):
    return namedtuple('X', geekDict.keys())(*geekDict.values())


# Suppose to JSON data
data = '{"name" : "Mustafa", "id" : 7, "location" : "Istanbul"}'

# making the object
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
y = json.loads(data, object_hook = customDecoder)
z = json.loads(data, object_hook = lambda d : Namespace(**d))


# accessing the JSON data as an object
print(x.name, x.id, x.location)
print(y.name, y.id, y.location)
print(z.name, z.id, z.location)