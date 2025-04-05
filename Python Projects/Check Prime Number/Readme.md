# 🔢 Prime Number Check Function

## 📚 Description
The function `is_prime` checks whether a given number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself.

---

## 📐 Function Definition

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
## ✅ Example Usage
```python
print(is_prime(11))  # True
print(is_prime(10))  # False
```
