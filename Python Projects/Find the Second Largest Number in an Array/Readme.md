# 🔢 Find the Second Largest Element in an Array

## 📚 Description
The function `second_largest` returns the second largest number in the given array. It removes duplicates and sorts the array before retrieving the second largest element. If there is no second largest element (e.g., array length is 1 or all elements are the same), it returns `None`.

---

## 📐 Function Definition

```python
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) > 1 else None
```
## ✅ Example Usage
```python
print(second_largest([10, 20, 4, 45, 99]))  # 45
```
