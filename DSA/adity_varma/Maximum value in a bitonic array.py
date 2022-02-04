arr = [1, 2, 4, 5, 20, 6, 3, 1]
low = 0
high = len(arr) - 1


def searching(arr, low, high):
    while low < high:
        mid = (low+high)//2
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid-1] < arr[mid]:
            low = mid+1
        else:
            high = mid-1

    return arr[low]


print(searching(arr, low, high))
