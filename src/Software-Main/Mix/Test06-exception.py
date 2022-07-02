"""
sayi1=12
sayi2=0

try:
    print(sayi1/sayi2)

except ValueError:
    print("sfira bolme hatasi")

except ZeroDivisionError:
    print("sfira bolnmez")

#veya string girilir ona gore hata yazdrilir gibi hata hngisisyse o except e girer
"""

try:
    dosya = open("yazlim blimi.txt","r")
except IOError:
    print("dsya blunamadi")
#finally tanmlayacagz cnku hta olmasa bazen dsya kapanmayablir bu gibi ihtimalleri dsnerek harekete gecicez
finally:
    dosya.close()
#boylece bufferda greksiz yer kaplamayacak
