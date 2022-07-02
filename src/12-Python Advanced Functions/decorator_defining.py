def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

def sayHello2():
    print("hello2")

sayHello = my_decorator(sayHello)
sayHello()

#burada fonk icinde fonk calgırıyor
#aynı ozelligi baska fonk eklemek icinde diger fonk cagırrız
#yani baska fonk ozellklerini direk ana fonksiyona ekledik

sayHello2 = my_decorator(sayHello2)
sayHello2()

#decorator fonksiyonların mantıgı bu fonksiyonlara belli ozellkleri eklemek baska yerden

#bunu decorator olarak kullanmak istersekte yani hayatımızda bldigimiz decorator altında bu varmıs yani
@my_decorator
def sayHello():
    print("hello")

sayHello()   # buda cagırmak icin bu kadar daha basit