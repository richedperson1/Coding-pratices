arr = [24,69,100,99,79,78,67,36,26,19]
high = len(arr)-1

# Method 1

def peak(arr, low, high):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid+1
        else:
            high = mid-1




print(peak(arr, 0, high=high))

# Method 2

def peak2(arr, low, high):
    while low < high:
        mid = (low+high)//2
        if arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid

    return low

print(peak2(arr, 0, high=high))