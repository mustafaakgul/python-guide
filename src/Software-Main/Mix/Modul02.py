
#internetten resm indirme
import urllib.request

url1=...
url2=...


urllist = [url1,url2]
counter=1

for url in urllist:
    urllib.request.urlretrieve(url,"resim"+str(counter)+".jpg")
    say+=1