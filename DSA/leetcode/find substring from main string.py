arr = [11, 13, 15, 17,1,2]

low = 0
high = len(arr)-1
n = len(arr)


def pivot_1(arr, low, high):
    while low < high:
        mid = (low+high)//2
        if arr[mid] > arr[high]:
            low = mid+1
        else:
            high = mid
    return low


print(pivot_1(arr, 0, len(arr)-1))