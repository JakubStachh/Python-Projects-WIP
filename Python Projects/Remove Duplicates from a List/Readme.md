# Remove Duplicates from List

## 📚 Description
This function `remove_duplicates` removes all duplicate elements from the provided list and returns a new list containing only the unique elements.

---

## 📐 Function Definition

```python
def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
```
## ✅ Example Usage
```python
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]
```
## 🧪 Example Output
```
[1, 2, 3, 4]
```
