message = 'Hello There. My name is Sadık Turan'
message = message.split()


# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip()
# message = message.split()
# message = message.split('.')
# message= '---'.join(message)

# index = message.find('Sadık')
# isFound = message.startswith('H') 
# isFound = message.endswith('n') 

# message = message.replace('Sadık','Çınar')
# message = message.replace('ç','c')
#                  .replace('ö','o')
#                  .replace(' ','-')

message = message.center(50,'*')

print(message)

"""
String'lerde Değer Atama(Variable Assignment)


Sayısal veri tiplerinde nasıl ki değer atayabiliyor, verilerin değerlerine isim verebiliyorsak, aynısını stringler için de yapabiliyoruz.


merhaba = "Merhaba nasılsın bugün?"


print(merhaba)
Merhaba nasılsın bugün?

String Concatenation


Operatörlerin uygulandıkları objelere göre değişik şeyler ifade edebileceğini konuşmuştuk.


+ operatörü sayısal veri tipleri üzerine etki edince toplama işlemi yapıyor. Ama uygulandığı objeler string ise yapacağı işlem concatenation (birleştirme) olacak. İki string'i art arta birleştirecek.


En çok karıştırılan durumlardan biri string olarak ifade edilen sayıları + operatörüne sokmak.


"5" + "4"
'54'


Python tırnak işareti içinde verdiklerimize karater olarak davrandığı için artık 5 ve 4 ü sayı olarak algılamıyor. + işlemi burada artık bu iki değeri yan yana koy demek, topla demek değil!


"hey"+"nasılsın?"
'heynasılsın?'


+ operatörünün tek yaptığı birleştirmek, stringlerde boşluk(space) olmadığı için ifadenin sonucu boşluksuz çıktı.


"hey" + " nasılsın?"
'hey nasılsın?'
"hey" + " " + "nasılsın?"
'hey nasılsın?'


Aynısını değer ataması yaparak da yapabilirdik


Diyelim ki karşılama mesajı yazmak istiyoruz. İsim ve karşılama kısmını ayrı tutacağız. Çünkü belki karşılayacağımız kişinin ismi değişecek ve ben kodumda sadece o değeri değiştirerek karşılama mantığını korumaya devam edeyim istiyorum.


mesaj = "Merhaba"



isim = "Berkay"


mesaj + " " + isim


'Merhaba Berkay'


Bu ifadenin değerini de başka bir değişkende tutabilirdik


karsilama = mesaj + " " + isim


print(karsilama)
Merhaba Berkay

Successive Concatenation(Ardışık Birleştirme)


* operatörü sayı objeleri için çarpım olarak tanımlanmışken, stringler için ard arda birleştirme işlemi yapıyor.


4 * "hey"
'heyheyheyhey'
"1" + "0" * 10
'10000000000'

len()


Bu metod ile (metodları ileride ayrıntılı olara göreceğiz), elimizdeki string'in kaç karakterden oluştuğunu öğrenebiliriz (boşluklar da karakter olduğu için onlar da sayılıyor)


len("4")
1
len("42")
2
len("hey")
3
len("hey!")
4
len("hey nasılsın?")
13
len(" ")
1
len("")
0

"""


"""
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
"""

#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# def split_and_join(line):
#     string = line.split(" ")
#     string = "-".join(string)
#     return string
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

boolean_value = "Moon" in "This text will describe facts and challenges with space travel"
print(boolean_value)

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
 while Mars has -28 Celsius."""
temperatures.find("Moon")
temperatures.count("Moon")
temperatures.lower().upper()

sentences = """aafawfgawdawdawdaw awdaw"""
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)