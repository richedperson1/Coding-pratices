arr = [6, 1, 5, 3, 2, 4, 2, 3, 6, 9, 7, 9, 21, 36, 98, 6, 46, 1003,0,2,36,9,3,9,7,6,1,3,4,98,66,1,6546,848,4984,8,18,548,48,465,1,498,498,1,84984654,1,65]

n = len(arr)
i = 0
total = 0
while i < n:
    for j in range(n-1):
        total+=1
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    i += 1
    n -= 1

print(arr)