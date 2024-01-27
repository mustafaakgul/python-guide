
import json


if __name__ =='__main__':

    person = '{"name": "Bob", "languages": ["English", "French"]}'
    person_dict = json.loads(person)

    # Output: {'name': 'Bob', 'languages': ['English', 'French']}
    print(person_dict)

    # Output: ['English', 'French']
    print(person_dict['languages'])

    person_dict = {'name': 'Bob',
                   'age': 12,
                   'children': None
                   }
    person_json = json.dumps(person_dict)

    # Output: {"name": "Bob", "age": 12, "children": null}
    print(person_json)

    x = """{
         "Name": "Jennifer Smith",
         "Contact Number": 7867567898,
         "Email": "jen123@gmail.com",
         "Hobbies":["Reading", "Sketching", "Horse Riding"]
         }"""
    json_object_personal =  '{ "name":"John", "age":30, "city":"New York"}'
    print(x, type(x))

    # Converting json str/string to dict(object)
    y = json.loads(x)
    print(y, type(y))
    print(y["Email"])

    z = json.loads(json_object_personal)
    print(z['age'])

    # dictionary(object) to be dumped
    d = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
    # which converts the Python objects(dictionary) into appropriate json objects
    with open('myfile.json', 'w', encoding='utf8') as json_file:
        json.dump(d, json_file, allow_nan=False)