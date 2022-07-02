# print("Hello")

#test.py to run python test.py


# class Problem:
#
#     @staticmethod
#     def fibonacci(n):
#         # Define the method
#         pass
#
# print(Problem.fibonacci(6))

#
# def isConsonant(ch):
#     # To handle lower case
#     ch = ch.upper()
#
#     return not (ch == 'A' or ch == 'E' or
#                 ch == 'I' or ch == 'O' or
#                 ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
#
#
# def totalConsonants(string):
#     count = 0
#
#     for i in range(len(string)):
#
#         # To check is character is Consonant
#         if (isConsonant(string[i])):
#             count += 1
#
#     return count
#
#
# # Driver code
# string = "abc dedfgrd"
# print(totalConsonants(string))


# def isConsonant(ch):
#     # To handle lower case
#     ch = ch.lower()
#
#     return not (ch == 'a' or ch == 'e' or
#                 ch == 'i' or ch == 'o' or
#                 ch == 'u') and ord(ch) >= 65 and ord(ch) <= 90
#
#
# def totalConsonants(string):
#     count = 0
#
#     for i in range(len(string)):
#
#         # To check is character is Consonant
#         if (isConsonant(string[i])):
#             count += 1
#
#     return count
#
#
# # Driver code
# string = "abc dedfgrd"
# print(totalConsonants(string))

"""
def ArrayChallenge(arr):
    test_str = arr
    all_freq = {}
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    counter=0
    for j in all_freq:
        if all_freq[j] == 1:
            counter = counter + 1

    if counter == len(test_str):
        #print("-1")
        return "-1"
    else:
        res = max(all_freq, key=all_freq.get)
        return str(res)
print(ArrayChallenge(input()))
"""

# def MathChallenge(strParam):
#     return int(eval(strParam.replace(")(", ")*(")))



# def isConsonant(ch):
#     # To handle lower case
#     ch = ch.upper()
#
#     return not (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
#
#
# def StringChallenge(string):
#     count = 0
#
#     for i in range(len(string)):
#         if (isConsonant(string[i])):
#             count += 1
#
#     return count
#
#
# # Driver code
# string = "mustafa"
# print(StringChallenge(string))






# def StringChallenge(string):
#     def isConsonant(ch):
#         ch = ch.upper()
#
#         return not (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
#
#     count = 0
#
#     for i in range(len(string)):
#         if (isConsonant(string[i])):
#             count += 1
#
#     return count
#
#
# # Driver code
# string = "Hello World"
# print(StringChallenge(string))


# def ArrayChallenge(arr):
#     new = ""
#     for x in arr:
#         new += str(x)
#     print(new)
#     test_str = new  #arr
#     all_freq = {}
#     for i in test_str:
#         if i in all_freq:
#             all_freq[i] += 1
#         else:
#             all_freq[i] = 1
#
#     counter=0
#     for j in all_freq:
#         if all_freq[j] == 1:
#             counter = counter + 1
#     #print(counter)
#
#     if counter == len(test_str):
#         #print("-1")
#         return "-1"
#     else:
#         res = max(all_freq, key=all_freq.get)
#         return str(res)
# print(ArrayChallenge([3,4,1,6,10]))


# Program to find most frequent
# element in a list

# def most_frequent(List):
#     counter = 0
#     num = List[0]
#     print("len", len(List))
#
#     for i in List:
#         curr_frequency = List.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             num = i
#
#     return num
#
#
# List = [2, 1, 2, 2, 1, 3, 5, 5, 5, 5]
# print(most_frequent(List))
#
# string = "merhaba"
# #print("merhaba"[10])  #getting error
# print("merhaba"[1:10]) #getting not error

# value = int(input("Enter a number: "))
# print(value)
# print(type(value))

# x=int(input("Ondalık bir sayı giriniz: "))  #0.25
# sonuc=x*4
# print(sonuc)

# x=int(float("3.9"))
#
# y=3
#
# print(x==y)

# print((True and True))
# print((True and False))
# print((False and True))
# print((True or False))

# x = (2==2) & print("merhaba")   #farkı short circuit olmadan and kullanmaktır
# print(x)

# sonuc = 1
# for i in range(4):
#     sonuc *= 3
# print(sonuc)
# # i hesaba katılmaz

# i=0
# while(i<10):
#     if(i==3 or i==5):
#       continue
#     print("i: ",i)
#     i=i+1

# a=20
# b=a
# a=a+5
# l=[20,30,40]
# l2=l
# l[0]=l[0]+5
#
# print(a)
# print(b)
# print(l2[0])

# x=5
# y=7
# temp=x
# y=temp
# print((x,y))

# d={"i":{2}}
# print(d)

# for i in range(2,5,3):
#     print(i)
#     #1 iterasyon

# dict
# mailler={'kisi1':"ad1.soyad1@gmail.com",'kisi2':"ad2.soyad2@gmail.com",'kisi3':"ad3.soyad3@gmail.com"}
# l=[]
# for v in mailler.values():
#     ",".join(l)
# l.append(v)
# #‘ad1.soyad1@gmail.com,ad2.soyad2@gmail.com,ad3.soyad3@gmail.com’

# x, y = 2, 4
# print(x, type(x))
# print(y, type(y))

