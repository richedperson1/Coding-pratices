def binary(arr, low, high, k):
    if low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid-1
            return binary(arr, low, high, k)

        else:
            low = mid+1
            return binary(arr, low, high, k)

    return -1


arr = [1, 2, 55, 66, 88, 895, 1002, 3696, 4002, 4023, 4115, 4203, 4245]
low = 0
high = len(arr)-1
k = 1002
print(binary(arr, low, high, k))
