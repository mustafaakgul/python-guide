

class Calisan():

    def __init__(self,isim,maas,departman):
        print("yapici snifi fonk")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def printinfo(self):
        #...
#kalitim yapmak
class Yonetici(Calisan):
    #overriding yeniden yzdgmz icin bu classdaki func cagrlcak yazmassan yukardakini kllnablrsn
    def __init__(self,isim,maas,departman,kisisaayisi):
        #icleri tekrar yazlablir yada ypmak istemiyorsak superi klln sadece farklılarını yaz
        super.__init__(isim,maas,departman)
        self.kisisayisi=kisisaayisi
        super.printinfo() # gibi seylrdede kllnalm ama fonk larnda tekrr yazlmasi grekeblr

yonetici = Yonetici():  #paramatreleri fln iceri grcen birde ek ozellkler eklenicek yoneticiye ozgu
yonetici.fonksiyonlar()
