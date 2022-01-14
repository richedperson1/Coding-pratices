arr = [2,4,10,10,10,50,60]

def first(arr,low,high,k):
    ans = -1
    while low<=high:
        mid = (low +high)//2
        if arr[mid]==k:
            ans = mid
            high = mid-1
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1

    return ans

def first1(arr,low,high,k):
    ans = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==k:
            ans = mid
            low = mid+1
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1

    return ans

n = len(arr)

print(first(arr,0,n-1,10))
print(first1(arr,0,n-1,10))