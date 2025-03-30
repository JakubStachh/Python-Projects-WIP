def missing_number(arr):
    n = len(arr) + 1
    return (n * (n + 1)) // 2 - sum(arr)

print(missing_number([1, 2, 3, 5]))  # 4
