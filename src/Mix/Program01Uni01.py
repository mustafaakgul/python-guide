
#video 54
import time
import sqlite3

class Ogrenci():

    def __init__(self):
        self.tablo_olustur()

    def tablo_olustur(self):
        self.baglanti = sqlite3.connect("ogrenciler.db")
        self.isaretci = baglanti.cursor()
        isaretci.execute("Create table if not exists ogrenciler (kisi TEXT, harf_notu TEXT,durum TEXT")
        self.baglanti.commit()

    def tablo_veri_ekle(self):
