import random
class Enemy:


    def __init__(self,name = "dusman",remainingHealth=1000,saldiriguc=20,mermisayisi=10):
        self.name = name
        self.remainingHealth = remainingHealth
        self.saldiriguc = saldiriguc
        self.mermisayisi = mermisayisi



    def print(self):
        print("basiliyor")
        print("isim : ",self.name,"kalan can",self.remainingHealth,"saldiri guc",self.saldiriguc,"mermi sayisi",self.mermisayisi)

    def attack(self):
        print("hucummm")
        print(self.name+"saldiriyor")
        harcananmermi=random.randrange(0,10)
        print(str(harcananmermi) +"kadarharcandi")
        self.mermisayisi-=harcananmermi
        #self.remainingHealth -= 1
        return (harcananmermi,self.saldiriguc)
#yani oar bi senaryo blirleyip onu koda dkmek koda dkmek kolay zten

    def mermibittimi(self):
        if (self.mermisayisi<=0):
            print(self.name+"bitti")
            return True
        return False

    def saldiriugra(self,harcananmermi,saldiriguc):
        self.remainingHealth-=harcananmermi*saldiriguc

    def isAlive(self):
        if(self.remainingHealth <= 0):
            print("dead")
        else:
            print(str(self.remainingHealth) + "remain health")

#enemy1 = Enemy()
#enemy2 = Enemy()
#print("dsman 1")
#enemy1.print()
#print("dsman 2")
#enemy2.print()
#enemy1.attack()
#enemy1.attack()
#enemy1.attack()
#enemy1.isAlive()

enemy1 = Enemy("ali",3000,31,45)
print("düsman1")
enemy1.print()
enemy2 = Enemy("veli",3500,43,56)
print("düsman2")
enemy2.print()
enemy3 = Enemy()
print("düsman3")
enemy3.print()

dusmanlar=[]

i=0
while(i<10):
    rastgelecan=random.randrange(100,200)
    #hepsini randoom olstur nesneleri brda yaray dnguyle ismide "dusman"+str(i+1)
    #dusmanlar.append nesneyi oraya ata veriyi orda tutalim
    #herhangi random dsmanlari savastrablirsin biseler yptirablirsin
for dusmann in dusmanlar:
    dusmann.print()
