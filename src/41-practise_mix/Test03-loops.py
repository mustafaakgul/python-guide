
"""
i=0
while(i<10):
    print("i degeri",i)
    i=i+2
    #i += 1

username = "mustafa"
password = "12345"

while(True):
    testUser = input("Username")
    testPass = input("Password")
    if ((username==testUser) and (password==testPass)):
        print("Welcome",username)
        break
    elif ((username!=testUser) and (password==testPass)):
        print("wrong username")
    elif ((username==testUser) and (password!=testPass)):
        print("remember pass")
        print("change pass Y/N")
        answer = input()
        if(answer == "Y"):
            newpass=input("new pass")
            print("wait a while")
            password=newpass
            print("pass is changed")
    else:
         print("try again")


string = "gollum"
list = ["elma", "armut"]

for i in range(10):
    print(i)
#range sırasyla olstran func

for j in range (1,10):
    print(j * "*")



facto=1

while True:
    number = int(input("sayi"))
    if(number<=0):
        print("negatf olmayan gir")
    else:
        for i in range(1,number+1):
            facto*=i
        print("faktoryel",facto)
        break



liste = [2,3,4]

for i in range(1,10):
    if(i in liste):
        continue
    print(i)

"""

i=0
while(i<10):
    if(i==2):
        continue
    i+=1
    #sonsuz dnguye grcek 2 olmicak cnku hc bir zaman

