import requests
from bs4 import BeautifulSoup

def sembolleritemizle(tumkelimeler):
    sembolsuzkelimeler = []
    semboller = "'^+%%/))=?/*"
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")    #kelimeden sembol atma icindeki sembolleri
                #video 44 pythondersleri 3 yazilim bilimi detayl

    #kelimenin kac defa dondugunu bulmak icin dict kullanlablir video 45

url = "https://www.cnnturk.com/turkiye/ankaraya-kar-geliyor-istanbulda-ise"

all_words = []

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

for kelimeGroups in soup.find_all("p"):
    #print(kelimeGroups)
    word_content = kelimeGroups.text
    words = word_content.lower().split()

    #print(words)
    for kelime in words:
        all_words.append(kelime)
        print(kelime)