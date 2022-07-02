
"""
import Modul01

Modul01.naber()
Modul01.mutlak(-10)

"""

from Modul01 import *
#yontemn tehlikesi su modul02 getirirsek ondada ayni metod olursa sknti kariikligi yapmassak sknti yok
#tum fonksiyonları almak yerine bllilerini alıp programı sknlestirebiliriz alt satrdaki
from Modul01 import naber

naber()
print(mutlak(-10))
print(mutlak(20))