arr = [1,2,3,4,8,6,2,0]
low = 0
high = len(arr)-1

def peark(arr,low,high):
    if low==high:
        return low
    else:
        mid = (low+high)>>1
        if arr[low]<arr[mid]:
            low = mid-1
            return peark(arr,low,high)

        else:
            high = mid
            return peark(arr,low,high)


print(peark(arr,low,high))