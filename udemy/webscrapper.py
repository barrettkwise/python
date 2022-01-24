import requests
import bs4
res = requests.get('http://quotes.toscrape.com/')
res.text
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('.author')
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)

soup.select('.text')
quotes = []
for name in soup.select('.text'):
    quotes.append(quotes.text)

soup.select('.tag-item')
tags = []
for item in soup.select('.tag-item'):
    tags.append(item.text)

url = 'http://quotes.toscrape.com/page/'

for page in range(1,10):
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)





