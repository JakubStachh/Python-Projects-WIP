# URL Shortener

## 📚 Description
This function `shorten_url` takes a long URL as input and returns a shortened version of the URL using the TinyURL service.

---

## 📐 Function Definition

```python
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

print(shorten_url("https://www.google.com"))
```
## ✅ Example Usage
```python
print(shorten_url("https://www.google.com"))  # Output: a shortened URL
```
## 🧪 Example Output
```
https://tinyurl.com/y5ev3vgy
```
