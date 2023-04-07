# we need to download beautiful soup
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)

# res.text returns too much data, we can clean it up using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')  # this returns a soup Object
# print(soup)
"""print(soup.body)
print(soup.contents)
print(soup.find_all('div'))
print(soup.find_all('a'))"""
print(soup.find(id='score_35481938'))
