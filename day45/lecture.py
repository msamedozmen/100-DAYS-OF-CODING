import requests
from bs4 import BeautifulSoup
import re

hacker_news = requests.get("https://news.ycombinator.com/news")

# print(hacker_news.text)


soup = BeautifulSoup(hacker_news.text,"html.parser")
aticle_titles = []
aticle_link=[]
all_titlell = soup.find_all(name ="a",rel="noreferrer")

for all_title in all_titlell:
    all_titles = all_title.getText()
    aticle_titles.append(all_titles)
    link=all_title.get("href")
    aticle_link.append(link)


upvoted = [re.sub("[^0-9]", "",upvote.getText()) for upvote in soup.find_all(name="span",class_="score")]


print(aticle_link)
print(aticle_titles)
print(upvoted)
