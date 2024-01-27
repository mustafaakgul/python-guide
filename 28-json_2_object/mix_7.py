import json
from typing import NamedTuple

_j = '{"name":"Иван","age":37,"mother":{"name":"Ольга","age":58},"children":["Маша","Игорь","Таня"],"married": true,' \
     '"dog":null} '


class PersonNameAge(NamedTuple):
    name: str
    age: int


class UserInfo(NamedTuple):
    name: str
    age: int
    mother: PersonNameAge
    children: list
    married: bool
    dog: str


j = json.loads(_j)
u = UserInfo(**j)

print(u.name, u.age, u.mother, u.children, u.married, u.dog)