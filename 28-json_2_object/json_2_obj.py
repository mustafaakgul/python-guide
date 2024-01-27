import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
print(data, type(data))

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)

# from recordclass import recordclass
# data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
#
# # Parse into a mutable object
# x = json.loads(data, object_hook=lambda d: recordclass('X', d.keys())(*d.values()))