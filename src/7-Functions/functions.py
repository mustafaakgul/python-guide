def voidfunc(hey):
    print(hey)

voidfunc("Hello")
#round(days_to_complete(238855, 75))

def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('mustafa')
msg = sayHello('akgul')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')


EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in
# the pass statement to avoid getting an error.
def myfunction():
  pass