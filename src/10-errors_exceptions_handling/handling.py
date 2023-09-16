# error handling => hata yönetimi

#BURADA TECRUBE KONUSUR BOLUMDE 0 A BOLME AKLIMIZA GELECEK VE BOYLE BIR CIKIS YOLU DEMEMIZ LAZIM
#VEYA BOLUMUNDE RAKAM YERINE 5D GIRDIN BOYLE BISEYDE OLAMAZ BUDA KONTROL EDILMELI YANI HER OLASILIK
#DUSUNULUP TRY CATH YAPILMALI
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('yanlış bilgi girdiniz')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')

#EN DUZGUN HALI BU
"""
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:    # burada exception en genel BASE yapı diger exceptionlar buradan turemis bu yuzden exception yazıp hangi exception olduunu print ile dondururuz logda fln
        print('yanlış bilgi girdiniz', ex)
    else:
        break
    finally:  # her zaman buraya girere calisir mesela dosya acıldı burada dosya kapanır
        print('try except sonlandı.')
"""

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError as e:
    print('payda 0 olamaz')
    print(e)
except ValueError:
    print("sayisal degerler olmali")
