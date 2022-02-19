arr = [[0, 1, 0],
       [0, 0, 0],
       [0, 1, 0]]

row = len(arr)
col = len(arr[0])

stack = []
for i in range(row):
    stack.append(i)

while len(stack)>1:
    first = stack[-1]
    stack.pop()
    second = stack[-1]
    stack.pop()
    if arr[first][second]:
        stack.append(second)
    else:
        stack.append(first)


cel = stack[-1]
sumi = sum(arr[cel])
total = 1
for i in range(row):
    if i==cel:
        continue

    elif arr[i][cel]!=1:
        total = 0
print(sumi)
if sumi==0 and total:
    print("Celebrity present : "+str(True))

else:
    print("Celebrity Not Present ")