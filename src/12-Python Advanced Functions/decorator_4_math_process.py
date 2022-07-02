#sunu kontrol edecegiz 2 tane operasyon var ama operasyonların surelerini hesaplancak
#fonksiyonlarda sadce islem yapılsın sure hesaplama o fonksiyona ait degildir bunu decoratorla yapalım birde decoratorsz

import math
import time

def usalma(a, b):
    start_time = time.time()
    time.sleep(1)
    print(math.pow(a,b))

    finish_time = time.time()
    print("fonksiyon" + str(finish_time - start_time))

def factorial(num):
    start_time = time.time()
    time.sleep(1)
    print(math.factorial(num))

    finish_time = time.time()
    print("fonksiyon" + str(finish_time - start_time))

usalma(2,3)
factorial(4)