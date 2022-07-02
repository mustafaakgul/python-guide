import json

input = ['foo', {'bar': ('baz', None, 1.0, 2)}]
new = json.dumps(input) # convert to JSON(str)
print(new, type(new), input, type(input))

# Converting from python object/dictionary to JSON string
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y, type(y))

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"), type(json.dumps("hello")))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

complex_model = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(complex_model))

#The json.dumps() method has parameters to make it easier to read the result:
print(json.dumps(complex_model, indent=2))
print(json.dumps(complex_model, indent=4))