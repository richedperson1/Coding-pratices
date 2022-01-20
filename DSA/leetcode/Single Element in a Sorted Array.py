nums = [1,1,2,3,3,4,4,8,8]
total = 0
high = len(nums)-1

def binary_search(arr,low,high):
    while low<high:
        mid = 2*((low+high)//4)
        if arr[mid]==arr[mid+1]:
            low = mid+2
        else:
            high = mid

    return low

print(binary_search(nums,0,high))