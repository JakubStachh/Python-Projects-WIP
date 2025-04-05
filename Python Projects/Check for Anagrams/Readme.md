# 🔠 Anagram Check Function

## 📚 Description
The function `is_anagram` checks whether two strings are anagrams. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

---

## 📐 Function Definition

```python
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
```

## ✅ Example Usage
```python
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```
