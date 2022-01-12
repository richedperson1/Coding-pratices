arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 3
a = arr[-k:]
arr[-3:] = [0]*k
for i in range(n-k-1,-1,-1):
    temp = arr[i]
    arr[i+k] = arr[i]

arr[:k]  = a
print(arr)