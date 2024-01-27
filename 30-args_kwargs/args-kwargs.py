
"""
metin1 = "merhaba dünya"
metin2 = "python dili"
metin3 = "arguman anlatimi"

baslik = "python programlama"

def metin_icerikleri(header,b,c,d):
    print("başlık : ",header)
    print(b)
    print(c)
    print(d)


metin_icerikleri(baslik,metin1,metin2,metin3)
"""

metin1 = "merhaba dünya"
metin2 = "python dili"
metin3 = "arguman anlatimi"

baslik = "python programlama"

def metin_icerikleri(header,*args):  #header harici tum ddegelri argman adndaki dgskende tutacak pointerda yani gelenlerin hepsini pointer gibi alir
    print(header)
    for metin in args:
        print(metin)

metin_icerikleri(baslik,metin1,metin2,metin3,9,87,"ali")



# argümana çevirerek yapalım
# def metin_icerikleri2(header,*args):
#     print(header)
#     for metin in args:
#         print(metin)
#
# metinler = [metin1,metin2,metin3]
#
# metin_icerikleri2(baslik,*metinler,metinler)