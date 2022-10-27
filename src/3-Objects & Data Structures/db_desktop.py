import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import StringVar
from tkinter import *

sqlarayuz= tk.Tk()
sqlarayuz.title("Hüseyin Yurdakul AVCİ 190706077")
sqlarayuz.iconbitmap('C:/Users/Aylin AVCİ/Desktop/icon.ico')
sqlarayuz.geometry("750x400")


def callback(deneme):

   content= deneme.get()
   sonuc = str(arama.get())
   for i in tv.get_children():
      tv.delete(i)
      db = pyodbc.connect(
         'Driver={SQL Server};'
         'Server=MateBook\SQLEXPRESS;'
         'Database=UniversiteyeBaslayanOgrenciler;'
         'Trusted_Connection=True;'

      )
      ogrenciler = db.cursor()
      ogrenciler.execute(f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")
      kullanicilar = ogrenciler.fetchall()
      count = 0
   for row in kullanicilar:
      tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
      count += 1
      print(row[0], row[1], row[2], row[3], row[4])
   if count==0:
      """yazısay = str(arama)
      test_str = (f"{yazısay}")
      counter = yazısay.count('')
      print("Count of e in GeeksforGeeks is : " + str(counter))"""

      arama.delete(0 , "end")
      sonuc = str(arama.get())

      db = pyodbc.connect(
         'Driver={SQL Server};'
         'Server=MateBook\SQLEXPRESS;'
         'Database=UniversiteyeBaslayanOgrenciler;'
         'Trusted_Connection=True;'

      )
      ogrenciler = db.cursor()
      ogrenciler.execute(
         f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")

      kullanicilar = ogrenciler.fetchall()
      count = 0
      for row in kullanicilar:
         tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
         count += 1
         print(row[0], row[1], row[2], row[3], row[4])
   print("Oldu")

#Create an variable to store the user-input
deneme = StringVar()
deneme.trace("w", lambda name, index,mode, var=deneme: callback(deneme))
#Create an Entry widget
arama = Entry(sqlarayuz, te=deneme)
arama.place(x=110,y=160)
aramayazi=tk.Label(sqlarayuz, text="Ara")
aramayazi.place(x=80,y=158)

#SQL Server Bağlantısı
db= pyodbc.connect(
    'Driver={SQL Server};'
    'Server=MateBook\SQLEXPRESS;'
    'Database=UniversiteyeBaslayanOgrenciler;'
    'Trusted_Connection=True;'

    )
ogrenciler=db.cursor()
ogrenciler.execute('SELECT * FROM Liste')
kullanicilar=ogrenciler.fetchall()


def ekle():
   db = pyodbc.connect(
      'Driver={SQL Server};'
      'Server=MateBook\SQLEXPRESS;'
      'Database=UniversiteyeBaslayanOgrenciler;'
      'Trusted_Connection=True;'

   )
   ogrenciler = db.cursor()
   cikarilacak = float(numaraekle.get())
   numara = str(numaraekle.get())
   ad = str(adekle.get())
   soyad = str(soyadekle.get())
   yas = str(yasetekle.get())
   cinsiyet = str(cinsiyetekle.get())
   komut = 'INSERT INTO Liste VALUES(?,?,?,?,?)'
   veriler = (numara, ad, soyad, yas, cinsiyet)
   sonuc = ogrenciler.execute(komut, veriler)

   sonuc = str(arama.get())
   for i in tv.get_children():
      tv.delete(i)
      ogrenciler.execute(
         f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")
      kullanicilar = ogrenciler.fetchall()
      count = 0
   for row in kullanicilar:
      tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
      count += 1
      print(row[0], row[1], row[2], row[3], row[4])

   print("Oldu")
   db.commit()


def cikar():
   db = pyodbc.connect(
      'Driver={SQL Server};'
      'Server=MateBook\SQLEXPRESS;'
      'Database=UniversiteyeBaslayanOgrenciler;'
      'Trusted_Connection=True;'

   )
   ogrenciler = db.cursor()
   cikarilacak = float(numaraekle.get())
   sonuc = ogrenciler.execute('DELETE FROM Liste WHERE Numara = ?', (cikarilacak))
   content = deneme.get()
   sonuc = str(arama.get())
   for i in tv.get_children():
      tv.delete(i)
      ogrenciler.execute(
         f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")
      kullanicilar = ogrenciler.fetchall()
      count = 0
   for row in kullanicilar:
      tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
      count += 1
      print(row[0], row[1], row[2], row[3], row[4])

   print("Oldu")
   db.commit()
   db.close()



def yenile():
   sonuc = str(arama.get())

   db = pyodbc.connect(
         'Driver={SQL Server};'
         'Server=MateBook\SQLEXPRESS;'
         'Database=UniversiteyeBaslayanOgrenciler;'
         'Trusted_Connection=True;'

      )
   ogrenciler = db.cursor()
   ogrenciler.execute(
         f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")

   kullanicilar = ogrenciler.fetchall()
   count = 0
   for row in kullanicilar:
      tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
      count += 1
      print(row[0], row[1], row[2], row[3], row[4])


def guncelle():
   db = pyodbc.connect(
      'Driver={SQL Server};'
      'Server=MateBook\SQLEXPRESS;'
      'Database=UniversiteyeBaslayanOgrenciler;'
      'Trusted_Connection=True;'

   )
   ogrenciler = db.cursor()
   cikarilacak = float(numaraekle.get())


   numara = str(numaraekle.get())
   ad = str(adekle.get())
   soyad = str(soyadekle.get())
   yas = str(yasetekle.get())
   cinsiyet = str(cinsiyetekle.get())
   sonuc = ogrenciler.execute('UPDATE Liste SET Adı = ?, Soyadı=?, Yaş=?,Cinsiyet=? WHERE Numara = ?',
                              (ad, soyad, yas, cinsiyet, numara))
   sonuc = str(arama.get())
   for i in tv.get_children():
      tv.delete(i)
      ogrenciler.execute(
         f"SELECT * FROM Liste Where Adı like '{sonuc}%' or Soyadı like '{sonuc}%' or Adı like '{sonuc}%' or Numara like '{sonuc}%' or Yaş like '{sonuc}%' or Cinsiyet like '{sonuc}%'")
      kullanicilar = ogrenciler.fetchall()
      count = 0
   for row in kullanicilar:
      tv.insert(parent='', index='end', iid=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
      count += 1
      print(row[0], row[1], row[2], row[3], row[4])

   print("Oldu")

   db.commit()


numaraekle=tk.Entry(sqlarayuz)
numaraekle.place(x=10,y=50)
nuamrayazi=tk.Label(sqlarayuz, text="Numara")
nuamrayazi.place(x=40,y=20)

adekle=tk.Entry(sqlarayuz)
adekle.place(x=160,y=50)
adyazi=tk.Label(sqlarayuz, text="Adı")
adyazi.place(x=205,y=20)

soyadekle=tk.Entry(sqlarayuz)
soyadekle.place(x=310,y=50)
soyadyazi=tk.Label(sqlarayuz, text="Soyadı")
soyadyazi.place(x=345,y=20)

yasetekle=tk.Entry(sqlarayuz)
yasetekle.place(x=460,y=50)
yasyazi=tk.Label(sqlarayuz, text="Yaş")
yasyazi.place(x=490,y=20)

cinsiyetekle=tk.Entry(sqlarayuz)
cinsiyetekle.place(x=610,y=50)
cinsiyetyazi=tk.Label(sqlarayuz, text="Cinsiyet")
cinsiyetyazi.place(x=630,y=20)




ekle=tk.Button(sqlarayuz, text="Ekle",command=ekle)
ekle.place(x=200,y=100)
cikar=tk.Button(sqlarayuz, text="Çıkar",command=cikar)
cikar.place(x=350,y=100)
guncelle=tk.Button(sqlarayuz, text="Güncelle",command=guncelle)
guncelle.place(x=500,y=100)

yenile=tk.Button(sqlarayuz, text="Tablonuz Silindiyde ve Aramalar Çalışmıyorsa Arama Kutusunu Silip Buraya Basınız",command=yenile)
yenile.place(x=215,y=340)



tv = ttk.Treeview( columns=(1, 2, 3, 4, 5), show='headings', height=8)
tv.pack()
tv.place(x=250,y=150)
tv.heading(1, text="No")
tv.heading(2, text="Ad")
tv.heading(3, text="Soyad")
tv.heading(4, text="Yaş")
tv.heading(5, text="Cinsiyet")
tv.column(1, width=30)
tv.column(2, width=100)
tv.column(3, width=100)
tv.column(4, width=50)
tv.column(5, width=100)


ogrenciler.execute('SELECT * FROM Liste')
kullanicilar = ogrenciler.fetchall()
count = 0
for row in kullanicilar:

    tv.insert(parent='', index='end', iid=count, text='', values=(row[0],row[1],row[2],row[3],row[4]))
    count += 1
    print(row[0],row[1],row[2],row[3],row[4])

sqlarayuz.mainloop()