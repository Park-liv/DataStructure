def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
a = [2, 5, 6, 7, 11, 23, 34, 34, 45, 56, 67, 88, 89, 90]
n = 56
print(binary_search(a, n, 0, len(a)-1))

a = [2, 5, 6, 7, 11, 23, 34, 34, 45, 56, 67, 88, 89, 90]
n = 86
print(binary_search(a, n, 0, len(a)-1))