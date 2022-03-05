arr = [-1,0,3,4] 

ele = 2

def binary(arr,low,high,k):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            high = mid-1
        else:
            low = mid+1

    return -1

def sum2ele(arr,ele):
    high = len(arr)
    for i in range(high):
        local = arr[i]
        tar = ele-local
        mid = binary(arr,i+1,high-1,tar)
        if mid>0:
            return [i+1,mid+1]
    else:
        return(-1)


print(sum2ele(arr,ele))