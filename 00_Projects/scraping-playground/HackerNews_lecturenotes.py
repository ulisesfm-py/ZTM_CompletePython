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
print(soup.find_all('a'))
print(soup.find(id='score_35481938'))"""

# one of the best ways to access specific data from the website is css selectors
# each website uses different classes
# this access class="score" of a website
votes = soup.select('.score')
# this access the titles of the articles
links = soup.select('.titleline')
# doing this returns a list of all the scores and titles

# we can keep selecting more specific things by using .get()
# we use votes[0] because it is a list, and we want the first item
print(votes[0].get('id'))

print(votes[0].value())
