#Using types.SimpleNamespace and object_hook  to convert JSON data Into a Custom Python Object

from __future__ import print_function
import json
from json import JSONEncoder
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

class Student:
    def __init__(self, rollNumber, name, marks):
        self.rollNumber, self.name, self.marks = rollNumber, name, marks

class Marks:
    def __init__(self, english, geometry):
        self.english, self.geometry = english, geometry

class StudentEncoder(JSONEncoder):
        def default(self, o): return o.__dict__

marks = Marks(82, 74)
student = Student(1, "Emma", marks)

# dumps() produces JSON in native str format. if you want to writ it in file use dump()
studentJsonData = json.dumps(student, indent=4, cls=StudentEncoder)
print("Student JSON")
print(studentJsonData)

# Parse JSON into an custom Student object.
studObj = json.loads(studentJsonData, object_hook=lambda d: Namespace(**d))
print("After Converting JSON Data into Custom Python Object using SimpleNamespace")
print(studObj.rollNumber, studObj.name, studObj.marks.english, studObj.marks.geometry)