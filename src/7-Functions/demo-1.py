# x=7
# def f(x):
#     res = 5
#     res*=res
#     if x%2==0:
#         print("Sonuc: ", res)
#
#         return res
#     else:
#
#         print("Sonuc: ", res)
#
#         return res + 10
#
# f(4)

# def square(x):
#     """
#     x'in karesini hesaplar
#     """
#     return x * x
#
# print(?square)


# if __name__ == '__main__':
#     n = int(input())
#     result_string = ""
#
#     for i in range(1, n + 1):
#         result_string += str(i) + ""
#     print(result_string)


# def f(x, y=True):
#
#     if x%2==0:
#
#         y=False
#
#         return y
#     return y
# print(f(7, True))


# l=["elma","portakal","armut"]
#
# m=l
#
# def f(y):
#     y[0]="limon"
#     return y
#
# f(l)
# print(m)
# print(l)


def kare(x):
    return x*x

def dikdortgen(x,y):
    return x*y

def alanlar_toplami(kare,dikdortgen):
    toplam_alan = kare(2) + dikdortgen(3,4)
