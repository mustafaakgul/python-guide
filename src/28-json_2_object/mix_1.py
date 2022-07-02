import json
from collections import namedtuple
from json import JSONEncoder

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

#Assume you received this JSON response
studentJsonData = '{"rollNumber": 1, "name": "Emma"}'

# Parse JSON into an object with attributes corresponding to dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(student.rollNumber, student.name)


def dict_to_class(class_name: Any, dictionary: dict) -> Any:
    instance = class_name()
    for key in dictionary.keys():
        setattr(instance, key, dictionary[key])
    return instance


def json_to_class(class_name: Any, json_string: str) -> Any:
    dict_object = json.loads(json_string)
    return dict_to_class(class_name, dict_object)
