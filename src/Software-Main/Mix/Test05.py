"""
#GLOBAL LOCAL
a=10
def func():
    global a=2
    print(a)

func()
print(a)
#global a olmassa a =2 dersek farkli snc ckar



#DICTIONARY
szluk = {"elma" : "meyve","armut" : "sebze"}

print(szluk["elma"])

for i in szluk.items():
    print(i)

dersler = {"ahmet" : ["veritabani","isletm sistem"],"oguz":["cebir","math"]}

for i in (dersler["ahmet"]):   #cuz this is a list
    print(i)
"""

#MODULS

