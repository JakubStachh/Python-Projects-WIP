# 🔄 Flatten a Nested List

## 📚 Description
The function `flatten_list` takes a nested list and returns a flat list with all the elements, regardless of how deeply they are nested. It recursively processes each item and extracts elements into a flat structure.

---

## 📐 Function Definition

```python
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
```
## ✅ Example Usage
```python
print(flatten_list([1, [2, [3, [4, 5]]]]))  # [1, 2, 3, 4, 5]
```
