import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
headlines = soup.find_all("h3")

for headline in headlines[:5]:
    print(headline.text)
