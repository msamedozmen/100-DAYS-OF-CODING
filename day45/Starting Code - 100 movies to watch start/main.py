import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
top100 = response.text

soup = BeautifulSoup(top100,"html.parser")

names =[name.getText() for name in soup.find_all("h3",class_="title")]

names=names[::-1]

# txt='\n'.join(names)

with open("TOP100 MOVIES.txt","w",encoding="utf-8") as file:
    for name in names:
        file.write(f"{name}\n")

# Write your code below this line 👇

# print(txt)
