arr = [5, 3, 6, 1, 2, 4,5]

n = len(arr)

for i in range(1,n):
    temp = arr[i]
    j = i-1

    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
    j+=1
    arr[j] = temp

print(arr) 