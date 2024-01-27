import bs4, requests
result = requests.get("https://www.api.github.com")
soup = bs4.BeautifulSoup(result.text)
elements = soup.select('title')

# Encoding in requests
print(result.encoding)