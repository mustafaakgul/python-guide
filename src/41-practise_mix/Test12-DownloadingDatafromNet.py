
import requests
from bs4 import BeautifulSoup

imdbUrl = "https://www.imdb.com/chart/top"

r = requests.get(imdbUrl)
soup = BeautifulSoup(r.content, "html.parser")

#artk parcalamaya baslarz sayfayi

receivingData = soup.find_all("table", {"class":"chart full-width"})

#print(receivingData)
#print(len(receivingData))
#sadece 1 tane tablo var cnku

#print(receivingData[0].contents)
#print(len(receivingData[0].contents))

#hangi tablo filmleri iceriyor

filmTable = (receivingData[0].contents)[len(receivingData[0].contents)-2]
#print(filmTable)
filmTable = filmTable.find_all("tr")

for film in filmTable:
    #print(film)
    filmtitle = film.find_all("td", {"class":"titleColumn"})
    #print(filmtitle)
    filmname=filmtitle[0].text
    filmname = filmname.replace("\n","")
    #her ters slash bos karekterle dgstrldi dzgn bir ifade oldu strng cnku bnlar
    print(filmname)

    #olay parcalamak parlamaka istedigimize ulasmak

