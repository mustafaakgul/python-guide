 # liste = [1,2,3,4,5]

# iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in liste:
#     print(i)

# liste = [1,2,3,4,5]
# iterator = iter(liste)

#asagıda for dongusunun nasıl iterator olusturdugu yazıyor mantıgı arkada while olusturup sonra cıkmak
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

#kenmizi iter next gibi seyleri ezerek veya altındaki calısma mantıgı ile
#kendi yapımızıı yazabiliriz munumbers ismi ile bunun yerine pyhon iterator
#kullanmak icin altta myiter=iter(list) de yeterli kendi fonk kullanablirzin
#kendi fonk ise dir ile gorebliriz
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

#custom ite kullanımı
list = MyNumbers(20,50)

#python kendi iter fonk kullanımı
myiter = iter(list)

# print(next(myiter))
# print(next(myiter))

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break


# for x in list:
#     print(x)

