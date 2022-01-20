arr = [0, 0, 0, 0, 1]
n = len(arr)
c = 0
for i in range(n):
    if arr[i] != 0:
        temp = arr[i]
        arr[i] = arr[c]
        arr[c] = temp
        c += 1

print(arr)
