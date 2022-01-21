arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

ele = 5

row = len(arr)
col = len(arr[0])

def binary(arr,low,high,ele):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==ele:
            return True
        elif arr[mid]>ele:
            high = mid-1
        else:
            low = mid+1

    return False

ans = -1
for i in range(row):
    if arr[i][0]<=ele and arr[i][-1]>=ele:
        ans = binary(arr[i],0,len(arr[i])-1,ele)
        break

print(ans)