arr = [2,1]
n = len(arr)-1
def peak_element(arr,low,high):
    if high==0:
        return arr[high]

    while low<high:
        mid = (low+high)//2

        if (mid>0 and mid<high) and arr[mid-1]<arr[mid]>arr[mid+1]:
            return mid
        
        elif arr[mid]<arr[mid+1]:
            low = mid+1
        else:
            high = mid-1

    return low

print(peak_element(arr,0,n))