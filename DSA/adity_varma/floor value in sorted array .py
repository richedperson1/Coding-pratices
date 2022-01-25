arr = [1, 2, 8, 10, 12, 19]
tar = 13
high = len(arr)-1
def floor_val(arr,low,high,ele):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=ele:
            low = mid+1
        else:
            high = mid-1

    return low-1

print(floor_val(arr,0,high,tar))