import requests
from bs4 import BeautifulSoup as bs

url = "https://www.amazon.com.au/s?k=books&crid=1BBWLPC2LDHO7&sprefix=boo%2Caps%2C347&ref=nb_sb_noss_2"
response = requests.get(url)
soup = bs(response.text, "lxml")
items = soup.find_all("div", class_ = "a-section a-spacing-small s-padding-left-small s-padding-right-small")
count = 1

def search(count=count):
    for i in items:
        itemName = i.find("a", class_ = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").text
        try:
            itemPriceDollar = i.find("span", class_ = "a-price-whole").text
        except(AttributeError):
            itemPriceDollar = "0"
        try:
            itemPriceCents = i.find("span", class_ = "a-price-fraction").text
        except(AttributeError):
            itemPriceCents = "00"
            

        
        print("{}) Item Name: {} Price: {}{}".format(count, itemName, itemPriceDollar, itemPriceCents))
        count += 1

search()