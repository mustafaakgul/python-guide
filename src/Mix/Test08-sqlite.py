import sqlite3

import random
import time
import datetime


"""

connection = sqlite3.connect("course.db")

cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, surname TEXT, no INT, studentNo INT)")
    #connection.commit()   #veritabaanini guncelleme islem yapildiktan snra bu yapilmali
    #connection.close()

def addValue():
    cursor.execute("INSERT INTO students VALUES ('mstafa','akgul',1234,78)")
    .execute("INSERT INTO students VALUES({},{},{})".format(isim,soyad,dogum))
    connection.commit()
    connection.close()

createTable()
addValue()

"""

connection = sqlite3.connect("course.db")

cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")


def addrandomvalue():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime = "python sqlite3"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    #tuple ile olusturmak
    connection.commit()
    # connection.close()

def getValues():
    #cursor.execute("SELECT * FROM Tablo1")
    #cursor.execute("SELECT zaman,tarih FROM Tablo1")
    cursor.execute("SELECT * FROM Tablo1 where deger = 4.0")
    data = cursor.fetchall()
    #print(type(data))
    #print(data)
    for i in data:
        print(i)

def Update():

    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Ilk Degerler ---------------------------------")
    for i in data:
        print(i)
    cursor.execute(("UPDATE Tablo1 SET deger=44 WHERE deger=7"))
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Guncel sonrasi ---------------------------------")
    for i in data:
        print(i)

    #dısardan parametri girceksek
    #update urunler set urunad = ? where urunad = ?",(eski isim,yeni isim)
    #

def delete():

    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Ilk Degerler ---------------------------------")
    for i in data:
        print(i)
    cursor.execute(("DELETE  FROM Tablo1 WHERE deger=1"))

    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Guncel sonrasi ---------------------------------")
    for i in data:
        print(i)
    connection.commit()

createTable()
#getValues()
#Update()
delete()

i=0
while(i<10):
    #addrandomvalue()
    time.sleep(1)   #to wait a while
    i+=1



connection.close()

