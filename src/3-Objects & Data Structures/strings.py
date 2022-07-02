name = 'Sadık'
surname = 'Turan'
age = 36

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting)

# print(greeting)
# print(greeting[0])
# print(greeting[3])
# print(greeting[length-1])
# print(greeting[-1])
# print(greeting[3:7])
# print(greeting[3:])
# print(greeting[:16])
print(greeting[2:40:3])


"""

String


Şimdiye kadar sadece sayılar ile uğraştık. Bu notebook'ta yeni bir veri tipine, String'lere bakalım


Stringler karakterlerden oluşan bir dizidir aslında. Stringlerin elemanları karakterlerdir.


Karakterler: (a,b,c,d...) gibi harfler, (*, ?, =, <, >, /...) gibi özel karakterler, (1,2,3...) gibi yazı biçiminde sayılar, boşluk(space) karakter olarak adlandırılabilir.


String'ler Karakterlerden veya bunların kombinasyonlarından oluşabilirler.


Bir şeyin String olduğunu belirtmek için yazacaklarımızı ikili tırnak ("örnek") veya tekli tırnak ('örnek') içine yazarız.


Tırnak işaretlerinin yaptığı şey aslında: Bu tırnak işaretlerinin içinde verdiğim diziye karakterler dizisi olarak davran, öyle algıla demek.


İkili tırnak içine de yazsak, tekli tırnak içine de yazsak aynı şekilde algılanır. Önemli olan hangisiyle başladıysak onunla bitirmek.


Scalar ve Non-scalar objelerden bahsetmiştik. Non-scalar veri tiplerinin daha alt parçalara bölünebilen, elemanlar içeren yapılar olduğunu konuşmuştuk. String non-scalar bir veri tipi. İçsel yapı olarak karakterlerden oluşuyor.


Stringler immutable veri tipidir.


Immutable: Elemanlarının değerleri değiştirilemez.


5
5
"5"
'5'
"a"
'a'
'a'
'a'
# Hangisiyle başladıysak onunla bitirmeliyiz
"a'
  File "<ipython-input-6-d24a784f7087>", line 2"a'
       ^
SyntaxError: EOL while scanning string literal
"5"
'5'
# Burada +'ya operatör olarak davranılmıyor, yazı olarak davranılıyor.
"5 + 10"
'5 + 10'
type('Hmm o zaman x=5 diyebilir miyiz?')
str
type("5")
str
type("5 + 10")
str


Hangisiyle başladıysak onunla bitireceğimiz için kesme işareti ve alıntı yapmada hangisiyle başladığımız önemli olabilir (bu ayrımı nasıl yapacağım, buna göre mi tasarlayacağım diyenler için iyi haber - escape character kısmını işleyince daha iyi bir yolunu göreceğiz)


"Bugün Kadıköy'e gidiyorum"
"Bugün Kadıköy'e gidiyorum"
'Bugün Kadıköy'e gidiyorum'
  File "<ipython-input-23-d2bbd68a7bc7>", line 1'Bugün Kadıköy'e gidiyorum'
                   ^
SyntaxError: invalid syntax




"Bana "Bugün Kadıköy'e gidiyorum" dedi"File "<ipython-input-25-c48935b23f4f>", line 1"Bana "Bugün Kadıköy'e gidiyorum" dedi"
               ^
SyntaxError: invalid syntax


'Bana "Bugün Kadıköy'e gidiyorum" dedi'
  File "<ipython-input-26-fa5558f0396a>", line 1'Bana "Bugün Kadıköy'e gidiyorum" dedi'
                         ^
SyntaxError: invalid syntax

Escape Sequence  : buna ' bir degisken gibi algılama escape yap bunu yapma backslach ile o character gec
"Bana \"Bugün ne yapıyorsun\" dedi"
'Bana "Bugün ne yapıyorsun" dedi'
'Bugün Kadıköy\'e gidiyorum'
"Bugün Kadıköy'e gidiyorum"

\  : burası backslach en sadece hali burada kacıyorsun
\n : new line : bu escape characterin özel bir hali
\\ : bu ise backslachdende kacın demek backslach goruncede  onu onemseme demek 
yani tek olunca ondan snrakini onemseme iki tane olunca benden snrakide bu oldugundan oenmseme
demek oluyor  - carpı - gibi aslnda

print("hey\nnasılsın")
hey
nasılsın
print("hey\tnasılsın")
hey nasılsın
print("hmm \")
> File "<ipython-input-32-98286fbc25b3>", line 1
    print("hmm \")
                  ^
SyntaxError: EOL while scanning string literal



print("hmm \\")


hmm \


mutable (they can be changed)
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).


"""
a="Bugün Mecidiyeköy\'den Mecidiyeköy'\e 40 dakikada gittim."
print(a)
print("Bugün Mecidiyeköy\'den Mecidiyeköy'\e 40 dakikada gittim." )

"""
You are given an immutable string, and you want to make changes to it.


"""


"""
You are given an immutable string, and you want to make changes to it.
string = "abracadabra"
print(string[5])
>>> string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
One solution is to convert the string to a list and then change the value.
string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
Another approach is to slice the string and join it back.
 string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra

def mutate_string(string, position, character):
    string = string[:position] + character + string[(position+1):]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
"""