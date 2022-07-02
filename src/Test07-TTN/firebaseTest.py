
from firebase import firebase

firebase = firebase.FirebaseApplication('https://lorawan-test-63445.firebaseio.com', None)
result = firebase.get('/users', None)
print(result)

