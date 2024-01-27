import typing

class User:
    name: str
    age: int

    def __init__(self, data: dict):
        for k, _ in typing.get_type_hints(self).items():
            setattr(self, k, data[k])

data = {
    "name": "Susan",
    "age": 18
}

user = User(data)
print(user.name, user.age)