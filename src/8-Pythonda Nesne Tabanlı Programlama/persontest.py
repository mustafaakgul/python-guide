
class Person:

    address = 'no information'
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

#    def __init__(self):
#        print('init2 metodu çalıştı.')
#Python does not support function overloading. When we define multiple functions with the same name, the later one
# always overrides the prior and thus, in the namespace, there will always be a single entry against each function name.


p1 = Person(name='ali', year= 1990)
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
p2 = Person()
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
