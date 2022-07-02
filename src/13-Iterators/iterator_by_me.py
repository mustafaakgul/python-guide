
list_4_iter = [2,3,4,5,6,7,8,]
#print(list_4_iter)
#print(dir(list_4_iter))  # dir ile kendi fonk goruruz

"""
for iter_object in list_4_iter:
    print(iter_object)
"""

iterator = iter(list_4_iter) #for yerine kendimiz bir iterator olusturduk iter den

print(iterator)
print(type(iterator))