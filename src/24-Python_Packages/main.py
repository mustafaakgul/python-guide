# Import hello module
import hello

import math as m
print("The value of pi is", m.pi)

#Instead of importing whole module
from math import e
print("The value of e is", e)

returning_type = hello.hello()
print(returning_type)
print(hello.var)

class_object = hello.function_class("mustafaakgul")
returning_str = class_object.__str__()
print(returning_str)

#Accessing Modules from Another Directory
#import sys
#sys.path.append('/home/mustafaakgul/Documents/Python_Packages')
#import hello
#Adding the Module to the Python Path
#python3
#import sys
#print(sys.path)