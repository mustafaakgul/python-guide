
import webbrowser
#webbrowser.open('https://python.org')
import bs4
import requests

result=requests.get('http://mas.bg.ac.rs')
result.raise_for_status()
x=result.text
#print(x)

#SiteSoup=bs4.BeautifulSoup(result.text)
#elements=SiteSoup.select('div')
#len(elements)

r = requests.get('https://api.github.com/events')
r.text
r.encoding