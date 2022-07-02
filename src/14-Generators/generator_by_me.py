"""
result = []
for i in range(5):
    result.append(i**3)

print(result) #burada degerler ramde tutulur

for i in range(5):
    yield i ** 3
"""
#yield degeri uretir sonra saklamaz bana yolar snucu bisey ypmaz daha siler

def cube():
    for i in range(5):
        yield i ** 3

generator = cube()
iterator = cube(generator)

print(next(iterator))
#burada 5 e kdar degildi 5000 olsaydı bellekte hic yer tahsil etmeden islem yapıp kaydetmeden cıkcaz
#BELLEK YONETIMI YAPMIS OLDUK CIDDI SEKILDE
#amac bir liste gibi birsy icinde saklamak gerekmiyorsa  o anda kullan at gibi bir seyde ise yarar