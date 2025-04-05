# 🔑 Password Generator

## 📚 Description
The function `generate_password` creates a random password of a given length, including characters from ASCII letters (uppercase and lowercase), digits, and punctuation. It ensures the password is both secure and randomly generated.

---

## 📐 Function Definition

```python
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password())
```
## ✅ Example Usage
```python
generate_password()  # Example output: 'uI#45tKg@9b!'
```
