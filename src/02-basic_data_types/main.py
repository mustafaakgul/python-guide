
#Scalar ans nonscalar: scalar kendi iclerinde parcalara ayrılan

"""
Integer
Float
Boolean
type()

Type Casting
int(2.4)
float()
"""

# x = -2.5
# print(x)
#
# print(int(4.8))

# string = "mustafa"
# string = string[:2] + "k" + string[3:]
# print(string)


# i = 4
# d = 4.0
# s = 'HackerRank '
#
# def split_and_join(line):
#     string = line.split(" ")
#     string = "-".join(string)
#     return string
#
# if __name__ == '__main__':
#     i = 4
#     d = 4.0
#     s = 'HackerRank '
#     var_int = input()
#     var_double = input()
#     var_string = input()
#     var_int = int(var_int)
#     var_double = float(var_double)
#     #result = split_and_join(line)
#     print(i + var_int)
#     print(d + var_double)
#     print(s + var_string)
#     print(var_int, var_double, var_string)
#     print()


# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#
# nterms = input("Pozitif sayi giriniz")
# nterms = int(nterms)
# # nterms = nterms-1
# index=[]
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))


# FibArray = [0, 1]
#
#
# def fibonacci(n):
#     # Check is n is less
#     # than 0
#     #
#     if n <= 0:
#         print("Incorrect input")
#
#     # Check is n is less
#     # than len(FibArray)
#     elif n <= len(FibArray):
#         print("elif")
#         return FibArray[n - 1]
#     else:
#         print("else")
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
#
#
# # Driver Program
# print(fibonacci(6))
# print(FibArray)


# def fib(n):
#     if n<0:
#         pass
#     else:
#         a = 0
#         b = 1
#         fibo=[]
#         if n == 1:
#             #print(a)
#             fibo.append(a)
#             #return n+1
#          el
#         else:
#             #print(a)
#             fibo.append(a)
#             #print(b)
#             fibo.append(b)
#             for i in range(2,(n+1)):
#                 c = a + b
#                 a = b
#                 b = c
#                 #print(c)
#                 fibo.append(c)
#         return fibo[-1]
# list_fivo = fib(2)
# print(list_fivo)
#
#
#
# class Problem:
#
#     @staticmethod
#     def fibonacci(n):
#             if n<0:
#                 pass
#             else:
#                 a = 0
#                 b = 1
#                 fibo=[]
#                 if n == 1:
#                     fibo.append(a)
#                 elif n==0:
#                     fibo.append(0)
#                 else:
#                     fibo.append(a)
#                     fibo.append(b)
#                     for i in range(2,(n+1)):
#                         c = a + b
#                         a = b
#                         b = c
#                         fibo.append(c)
#                 return fibo[-1]
#
# print(Problem.fibonacci(6))

class Problem:

    @staticmethod
    def foobar(n):
        array = []
        for i in range(1,n+1):
            if i%15==0:
                #print("foobar")
                array.append("foobar")
            elif i%3==0:
                #print("foo")
                array.append("foo")
            elif i%5==0:
                #print("bar")
                array.append("bar")
            else:
                #print(i)
                array.append(str(i))
        return array

print('\n'.join(Problem.foobar(8)))



"""
class Problem:

    @staticmethod
    def foobar(n):
        # Define the method
        return []

print('\n'.join(Problem.foobar(5)))
"""