from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=header)

data = response.text

soup = BeautifulSoup(data,"html.parser")

all_links_element = soup.select("#grid-search-results a")

all_links = []
for link in all_links_element:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_adress_elements = soup.select("#grid-search-results a address")
all_adress = []
all_addresses = [address.get_text().split(" | ")[-1] for address in all_adress_elements]



all_price_elements = soup.select(".kSsByo")
print(len(all_price_elements))
all_prices = []
# for element in all_price_elements:
#     # Get the prices. Single and multiple listings have different tag & class structures
#     try:
#         # Price with only one listing
#         price = element.select(".list-card-price")[0].contents[0]
#     except IndexError:
#         print('Multiple listings for the card')
#         # Price with multiple listings
#         price = element.select(".list-card-details li")[0].contents[0]
#     finally:
#         all_prices.append(price)

# print(all_prices)


# print(all_addresses)
# print(len(all_adress))
# print(len(all_links))