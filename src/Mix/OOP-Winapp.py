#muzik calar mert mekatronik video 32
import time
import random

class Winapp():

    def __init__(self,sarkilar = [], durum = True):
        self.sarkilar = sarkilar
        self.durum = durum
        self.ses = 100
        self.calanSarki = ""

    def sesArttir(self):
        if(self.ses >= 95):
            pass
            #self.ses = 100
        else:
            print("Ses arttiriliyor")
            time.sleep(1)
            print("Ses arttirildi Guncel ses : {}".format(self.ses))
            self.ses += 5

    def sesAzalt(self):
        if(self.ses <= 0):
            pass
        else:
            self.ses -=5

    def sarkiekle(self,sarki):
        self.sarkilar.append(sarki)
    def sarkiSec(self,secim):
        sayac = 1
        for i in self.sarkilar:
            print("{} . {}".format(sayac,i))
        secim = int(input("sarki no"))
        self.calanSarki = self.sarkilar[secim-1]

    def sarkiListesi(self):
        print(self.sarkilar)
#pop ile sarki silme de olablr
    def rastgelesarki(self):
        rastgelesayi = random.randint(0,len(self.sarkilar))
        self.calanSarki = self.sarkilar[rastgelesayi]
    def winappkapa(self):
        self.durum = False
    def arayuz(self):
        print("""
              sarki listesi = {}
              su an calan sarki = {}
              ses = {}
              durum = {}
              
              1-sarki sec
              2-ses arttir
              3-ses azalt
              4-rantgelesarkisec
              5-sarki ekle
              
              
        
        """.format(self.sarkilar.self.calanSarki#.....))

o1 = Winapp(sarkilar= ["sarki1"])

while True:
    o1.arayuz()
    secim = int(input("seciminiz"))
    if(secim ==1):
        o1.sarkiSec()
        #gbi gibi seyler yapılcak