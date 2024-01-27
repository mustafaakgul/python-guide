
#https://pypi.org/project/json2object/

from json2object import jsontoobject as jo

class Student:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.courses = [Course('')]

class Course:
    def __init__(self, name):
        self.name = name

data = '''{
"firstName": "James",
"lastName": "Bond",
"courses": [{
    "name": "Fighting"},
    {
    "name": "Shooting"}
    ]
}
'''

model = Student()
result = jo.deserialize(data, model)
print(result.courses[0].name)