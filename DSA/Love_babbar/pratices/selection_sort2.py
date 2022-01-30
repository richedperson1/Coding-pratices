arr = [64,5,2,10,99,8]

n = len(arr)
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

for i in range(n-1):
    temp = i
    for j in range(i+1,n):
        if arr[temp]>arr[j]:
            temp = j
        
    arr = swap(arr,temp,i)

print(arr)