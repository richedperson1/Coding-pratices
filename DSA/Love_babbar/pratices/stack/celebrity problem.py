arr = [[0, 1, 0],
       [0, 1, 0],
       [0, 0, 0]]

row = len(arr)
col = len(arr[0])
celebrity = -1
for i in range(row):
    total = 0
    for j in range(col):
        total+=arr[i][j]

    if total==0:
        celebrity = i
        break

total = True

for i in range(row):
    if i==celebrity:
        continue
    if arr[i][celebrity]!=1:
        total = False
    


if total:
    print("yess their is a celebrity")

else:
    print("NO celebrity are their")