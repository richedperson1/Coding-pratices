arr = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

ele = 0

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
        if ans:
            print(True)
            # exit
            exit()

print(False)