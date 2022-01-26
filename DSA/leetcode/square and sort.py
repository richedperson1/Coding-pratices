def sure(arr):
    n = len(arr)
    high = n-1
    low = 0
    result = [0]*n
    for p in range(n-1,-1,-1):
        if abs(arr[low])<abs(arr[high]):
            result[p] = arr[high]**2
            high-=1
        else:
            result[p] = arr[low]**2
            low+=1
            
    return result

arr = [-4,-1,0,3,10]
print(sure(arr))