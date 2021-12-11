
def binary_search(arr,low,high,ele):
    while low<= high:
        mid = (low+high)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            high = mid-1
        else:
            low = mid+1
    return -1

def pivot_1(arr,low,high):
    while low<high:
        mid = (low+high)//2
        if arr[mid]>=arr[0]:
            low = mid+1
        else:
            high = mid
    return low

def findPosition(arr, n, k):
    ele = k
    high = n-1
    pivot =  pivot_1(arr,0,n-1)
    if arr[pivot]<=ele and arr [high] >=ele:
        return(binary_search(arr,pivot,high,ele))
    else:
        return(binary_search(arr,0,pivot-1,ele))


	
arr = [8,1,2,4,6]
n = len(arr)-1
print(findPosition(arr,n,8))