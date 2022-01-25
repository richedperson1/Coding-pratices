arr = [1,1,1,1,1,1, 2, 8, 10, 12, 19]
tar = 1.3
high = len(arr)-1
def floor_val(arr,low,high,ele):
    result = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=ele:
            result = mid
            low = mid+1
        else:
            high = mid-1

    return result

print(floor_val(arr,0,high,tar))