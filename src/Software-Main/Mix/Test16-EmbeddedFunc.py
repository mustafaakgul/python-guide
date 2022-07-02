from functools import reduce

#map()
#reduce()
#min()
#max()
#------------

isci = ["ahmet","mehmet"]
maas = [2000,3000]
print(list(zip(isci,maas)))

#ORRRRRRRRRRRRRRR

def eslestir(liste1,liste2):
    liste = list()
    for i in range(len(liste1)):
        liste.append((liste1[i],liste2[i]))
    return liste

eslestir(isci,maas)

a = list(enumerate(["istanbul","ankara"]))
print(a)

filter()