arr = [100, 80, 60, 70, 60, 75, 85]
n = len(arr)
vector = []

stack = []
total = 1
for i in range(n):
    if not stack:
        vector.append(-1)
        stack.append(i)

    elif arr[stack[-1]]>arr[i]:
        vector.append(stack[-1])
        stack.append(i)

    else:
        while len(stack)>0 and arr[stack[-1]]<arr[i]:
            stack.pop()

        if not stack:
            vector.append(0)
            stack.append(i)
        else:
            vector.append(stack[-1])
            stack.append(i)

for i in range(n):
    vector[i] = i-vector[i]

print(vector)