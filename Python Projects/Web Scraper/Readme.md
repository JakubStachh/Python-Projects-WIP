# Web Scraping BBC Headlines

## 📚 Description
This script uses the `requests` and `BeautifulSoup` libraries to scrape the top 5 headlines from the BBC homepage. It fetches the page content, parses the HTML, and extracts the text from the `<h3>` tags, which are often used for headlines.

---

## 📐 Function Definition

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
headlines = soup.find_all("h3")

for headline in headlines[:5]:
    print(headline.text)
```
## ✅ Example Output
The output will display the top 5 headlines from the BBC homepage:
```
"Headline 1"
"Headline 2"
"Headline 3"
"Headline 4"
"Headline 5"
```
## 💡 Explanation
- **Requests**: The `requests.get(url)` function is used to fetch the page content from the BBC website.

- **BeautifulSoup**: `BeautifulSoup(page.content, "html.parser")` parses the HTML content of the page.

- **Finding Headlines**: `soup.find_all("h3")` finds all the `<h3>` tags on the page, which typically contain the headlines.

- **Looping**: The script loops through the first 5 `<h3>` tags and prints the text content of each headline using `.text`.
