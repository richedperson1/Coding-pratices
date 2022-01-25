arr = [1,1,1,1,1,2,2,2,2]
tar = 1.2
high = len(arr)-1
def ceil_value(arr,low,high,ele):
    result = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=ele:
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result

print(ceil_value(arr,0,high,tar))