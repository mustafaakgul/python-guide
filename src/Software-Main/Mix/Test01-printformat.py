
print("program ismi")
a = input()
print(a)

b = input("birsayigirin : ")
print(b)
info = [a,b]

print("kaydedildi") #belli kontrol noktaları veya debuglarla bralarda ne yapiyor gibi

print("sayilarin toplami",int(a)+int(b))

print("oyuncu adi: {}\n oyuncu soyadi: {}".format(info[0],info[1]))
#ters slashlar gerekli operasynlari yapar