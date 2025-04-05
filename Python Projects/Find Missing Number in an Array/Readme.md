# 🧩 Missing Number in Array

## 📚 Description
The function `missing_number` finds the missing number from an array of integers that contains numbers from 1 to `n` with one missing number. It uses the formula for the sum of the first `n` natural numbers to calculate the expected sum and subtracts the sum of the elements in the array from it.

---

## 📐 Function Definition

```python
def missing_number(arr):
    n = len(arr) + 1
    return (n * (n + 1)) // 2 - sum(arr)
```
## ✅ Example Usage
```python
print(missing_number([1, 2, 3, 5]))  # 4
```
