import requests
from bs4 import BeautifulSoup
import pandas as pd

# proxies = {
#     'http': '127.0.0.1:8118',
#     'https': '127.0.0.1:8119'
# }

data = {"Title":[],"Price":[]}

url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r =  requests.get(url,proxies=proxies)
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())

spans = soup.select("div._4rR01T")

prices = soup.select("div._25b18c")

for span in spans:
    print(span.string)
    data["Title"].append(span.string)

for price in prices:
    print(price.find("div").get_text())
    data["Price"].append(price.find("div").get_text())
    if len(data["Price"])==len(data["Title"]):
        break

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)