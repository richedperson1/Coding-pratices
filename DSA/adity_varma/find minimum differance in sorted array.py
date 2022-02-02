arr = []
k = 7
def positive_mini(arr,low,high,k):
    if high <=0:
        return -1
    result = 0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=k:
            result = mid
            low = mid+1

        else:
            high = mid-1

    return arr[result]
def positive_maxi(arr,low,high,k):
    if high<=0:
        return -1
    result = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=k:
            result = mid
            high = mid-1

        else:
            low = mid+1

    return arr[result]

high = len(arr)-1

second = positive_maxi(arr,0,high,k)
first = positive_mini(arr,0,high,k)
print(second,first)