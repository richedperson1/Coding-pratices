def linear_search(arr, k):
    n = len(arr)
    if n == 0:
        return False

    if arr[0] == k:
        return True
    return linear_search(arr[1:], k)


arr = [1, 2, 3, 6, 4, 6, 9, 7]


print(linear_search(arr, 1))
