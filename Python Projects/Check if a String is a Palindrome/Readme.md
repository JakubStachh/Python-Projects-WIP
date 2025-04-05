# 🏁 Palindrome Check Function

## 📚 Description
The function `is_palindrome` checks whether a string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward (ignoring spaces, punctuation, and capitalization).

---

## 📐 Function Definition

```python
def is_palindrome(s):
    return s == s[::-1]
```

## ✅ Example Usage
```python
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```
