# 🧮 Fibonacci Sequence

## 📚 Description
The function `fibonacci` generates the first `n` numbers of the Fibonacci sequence. Each number is the sum of the two preceding ones, starting from 0 and 1. It prints the sequence on the same line.

---

## 📐 Function Definition

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
```

## ✅ Example Usage
```python
fibonacci(7)  # 0 1 1 2 3 5 8
```
