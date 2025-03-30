def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) > 1 else None

print(second_largest([10, 20, 4, 45, 99]))  # 45
