from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re

url = "https://www.yahoo.co.jp"
r = requests.get(url)
#time.sleep(3)

soup = BeautifulSoup(r.text, "html.parser")
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for elem in elems:
    print(elem.span.string)
    print(elem.attrs['href'])