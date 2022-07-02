# squares = [i * i for i in range(1,11)]
# print(squares)

m=[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]
print(m)

new = [i for l in m for e in l for i in e]

print(new)