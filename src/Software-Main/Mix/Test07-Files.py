"""
#dosya yapilarini gormek,bnn yerine path de verileblir
file = open("yazilim.txt", "a")

file.write("npiyon")


#otomatik is biitince python dosya kapama
with open("yazilim.txt","r") as file:
    print(file.read())


#dosyalari efektif okumak
with open("yazilim.txt","r") as file:
    file.seek(10)         # 10 dersen ilk 10 karekterden snra okumaya baslar
    print(file.read())    # readin icinde 5 yzarsak 5 tane okur
    file.seek(5)
    str1 = file.read(5)   #string atamalari


#dosyada dgsklk
with open("yazilim.txt","r+") as file:
    data=file.read()
    file.seek(0)
    data="ppapdap\n" + data
    file.write(data)
    #file.write("asdasda") # bu direk en sona ekler




#dosyann ortasna bi yere eklemek icin de

liste = [1,2,3,4,5]
liste.insert(1,15)
#1. indexe 15 ekle
print(liste)

"""


with open("yazilim.txt","r+") as file:
    data = file.readlines()
    data.insert(1,"php : aadwdawd")    #ortasna data eklemek
    file.seek(0)
    file.writelines(data)



try :
    dosya = open("bilgi.txt","r")
    icerik = dosya.read()


    dosya.close()

except FileNotFoundError:
    print("boyle dosya yok")

try:
    with open ("file.txt","r+") as file:     #hem okuma hem yazmak
        print(file.tell())    #cursorn nerede oldugunu gosterir
        a=file.read()
        file.seek(5)   # 5. inci byte git
        print(a)


except FileNotFoundError:
    print("boyle dosya yok")



