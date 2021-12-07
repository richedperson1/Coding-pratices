arr = [0,1,2,5,3]
brr = [0,0,1,2,3]
def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    i = 0
    j = 0
    res = []
    while i<n and j<m:
        if arr[i] == brr[j]:
            res.append(arr[i])
            arr[i] = -1
            brr[j] = -2
            i+=1
            j+=1
        elif arr[i] > brr[j]:
            j+=1
        elif arr[i]<brr[j]:
            i+=1      
    return res


print(findArrayIntersection(arr,len(arr),brr,len(brr)))