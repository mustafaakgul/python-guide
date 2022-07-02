baslik = "python programlama"

def metin_icerikleri(header,**kwargs):
    print("başlık : ", header)
    for metin in kwargs.items():
        print(metin)

metin_icerikleri(baslik,
                 metin1 = "merhaba dünya",
                 metin2 = "python dili",
                 metin3 = "arguman anlatimi")

#argumanda kendisinn dgerini ylluyrsn
#kwarg szlk gibi isim ve degeri gibi keywordlu gndermde