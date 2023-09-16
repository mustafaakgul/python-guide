import sys

mert = 20
ahmet = 20
ram1 = sys.getrefcount(mert)
print(ram1)
ram2 = sys.getrefcount(ahmet)
print(ram2)

def print_mert(bisey):
    print(bisey)