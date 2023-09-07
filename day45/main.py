
from bs4 import BeautifulSoup

with open("website.html",encoding="utf8") as file:
    contents = file.read()

# print(contents)
    
soup = BeautifulSoup(contents,"html.parser")

# print(soup.prettify())

paragps =soup.find_all("a")
for p in paragps:
    print(p.getText())
    print(p.get("href"))
    
company_url = soup.select_one("p a")
print(company_url)