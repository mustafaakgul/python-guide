# fruits = { 'orange', 'apple', 'banana'}
#
# # print(fruits[0]) indekslenemez
#
# for x in fruits:
#     print(x)
#
# fruits.add('cherry')
# fruits.update(['mango','grape','apple'])
#
# fruits.remove('mango')
# fruits.discard('apple')
# fruits.pop()
#
# fruits.clear()
#
# print(fruits)
#
# # myList = [1,2,5,4,4,2,1]
# # print(myList)
# # print(set(myList))


s = set([1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for element in s:
    #print(element)
    pass

#s.remove(15)  # getting KeyError: 15 so it must be in try block
print(s)
print(type(s))
print(s.remove(3))

try:
    s.remove(20)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)
    print("5 not found")


# .remove(x)
# This operation removes element  from the set.
# If element  does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
# .discard(x)
# This operation also removes element  from the set.
# If element  does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.
# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.