
#https://pypi.org/project/dataclass-wizard/

from dataclasses import dataclass

from dataclass_wizard import fromdict, asdict


@dataclass
class User:
    name: str
    age: int
    is_active: bool


data = {
    'name': 'John',
    'age': 30,
    'isActive': True,
}

user = fromdict(User, data)
assert user == User(name='John', age=30, is_active=True)

json_dict = asdict(user)
assert json_dict == {'name': 'John', 'age': 30, 'isActive': True}