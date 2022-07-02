
"""
def hello():
    print("hello")

#hello()

def fact(number):
    facto= 1
    for i in range(1,number+1):
        facto *= i
    print("facto",facto)

#sayi = int(input("sayi gir"))
#fact(sayi)
#fact(6)

def fact(number):
    facto= 1
    for i in range(1,number+1):
        facto *= i
    return facto

a=fact(5)
print(a)



def register(ad="no info", soyad="no info"):
    print("kayt eklenyr")

    print("ad:{}\nsoyad:{}".format(ad,soyad))

    print("eklendi")

register("mstafa")

"""

#recursion func

def topla(liste):
    toplam = 0

    for i in liste:
        toplam+=i
    return toplam

print(topla([1,2,3,4,5]))

def topla2(liste):
    if(len(liste)) == 0:
        return 0
    else:
        return liste[0] + topla2(liste[1:])

print(topla([1,2,3,4,5,6]))

def tamsayibolenleri(sayi):
    liste = list()
    for i in range(1,sayi+1):
        if sayi%i==0:
            liste.append(i)
    return liste

print(tamsayibolenleri(1245))
#ebob ekok fonksiyonu
