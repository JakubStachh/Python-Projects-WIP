# 🧮 Factorial Function

## 📚 Description
The function `factorial` calculates the factorial of a number `n`. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 (denoted as 5!) is `5 * 4 * 3 * 2 * 1 = 120`.

---

## 📐 Function Definition

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
```
## ✅ Example Usage
```python
print(factorial(5))  # 120
print(factorial(0))  # 1
```
