def linear_search(arr, k):
    n = len(arr)
    if n == 0:
        return False

    if arr[0] == k:
        return True
    return linear_search(arr[1:], k)

def linear_search(arr,low, k):
    n = len(arr)
    if low == n:
        return False

    if arr[low] == k:
        return low
    linear_search(arr,low+1,k)
    print(low)



arr = [1, 2, 3, 6, 4, 6, 9, 7]


(linear_search(arr,0, 9))
