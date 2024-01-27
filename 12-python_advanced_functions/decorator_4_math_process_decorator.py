#sunu kontrol edecegiz 2 tane operasyon var ama operasyonların surelerini hesaplancak
#fonksiyonlarda sadce islem yapılsın sure hesaplama o fonksiyona ait degildir bunu decoratorla yapalım birde decoratorsz
#oncekinin decoratorlu olanı
#fonksiyonların icini bosalttık fonk olması grektifi gibi gercek hayattada sadece yapması gerekni yapcak

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish_time = time.time()
        print("fonksiyon" + func.__name__ + str(finish_time - start_time))
    return inner()

@calculate_time
def usalma(a, b):
    print(math.pow(a,b))

@calculate_time
def factorial(num):
    print(math.factorial(num))

usalma(2,3)
factorial(4)