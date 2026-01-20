import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.findAll('div')) #scrape any info like a tags,div, title , class & id etc
