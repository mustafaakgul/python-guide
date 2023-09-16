"""
Operatörler ve İfadeler (Operators-Expressions)


Objeler(object) ve operatörlerin(operator) birleşimi expression'ları oluşturur.


Expression'ların değerleri (value)'ları vardır ve tabii ki de bunların tipleri vardır.


İfadeler şöyler oluşturulur: (object) (operator) (object)


Expression'ların tiplerini operator'un uygulandığı objelerin tipleri belirler.

+ operator
# İki tane integer'ın toplamı integer verir.
2 + 2
4
type(2+2)
int
# İki tane float'un toplamı float verir.
2.4 + 2.5
4.9
type(2.4 + 2.5)
float


Eğer objelerden biri bile float ise toplama işleminde expression'un tipi float olur.


2.4 + 3
5.4
type(2.4 + 3)
float

- operator


# İki tane integer'ın farkı integer verir.
3 - 2
1
type(3-2)
int
# İki tane float'un farkı float verir.
2.6 - 2.1
0.5
type(2 - 2.1)
float


Eğer objelerden biri bile float ise çıkarma işleminde expression'un tipi float olur.


2.5 - 3
-0.5
type(2.5 - 3)
float

* operator


# İki tane integer'ın çarpımı integer verir.
3 * 2
6
type(3*2)
int
# İki tane float'un çarpımı float verir.
2.6 * 2.4
6.24
type(2.6 * 2.4)
float


Eğer objelerden biri bile float ise çarpma işleminde expression'un tipi float olur.


2.5 * 3
7.5
type(2.5 * 3)
float

/ operator


İşleme giren objelerin tipi ne olursa olsun cevap float olur.


3 / 2
1.5
3 / 1.5
2.0
2.4 / 0.6
4.0

// operator (int division)


Eğer işleme girenlerden biri bile float ise cevap float olur.


5 // 2
2
5 // 2.5
2.0
4.2 // 5
0.0
8.2 // 5
1.0

% operator (Remainder/kalan)


Eğer kalan float ise cevap float olur yoksa integer olur.


5 % 2
1
10 % 3
1
2.5 % 2
0.5

** operator


Üst alma işlemi yapar.


2 ** 3
8
3 ** 2
9
2.4 ** 2
5.76
5 ** -1
0.2

print()


Bazen sadece bazı değerleri bastırmak isteriz, bunun için print() metodunu kullanabiliriz.


print(5)
5
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print("hey")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python Arithmetic Operators
# Python Assignment Operators
# Python Comparison Operators
# Python Logical Operators
# Python Identity Operators
# Python Membership Operators : in, not in
# Python Bitwise Operators