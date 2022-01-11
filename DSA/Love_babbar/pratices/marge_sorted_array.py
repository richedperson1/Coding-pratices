arr = [1, 2, 3, 0, 0, 0]
arr1 = [2, 5, 6]
m = 3
n = 3
while m>=n and n>0:
    if m ==0:
        arr[:n] = arr1[:n]

    elif arr[m-1]>arr1[n-1]:
        arr[m+n-1] = arr1[n-1]
        m-=1
    else:
        arr[m+n-1] = arr1[n-1]
        n-=1

print(arr)