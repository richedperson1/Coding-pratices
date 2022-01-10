def maximum_area(arr, n):
    stack = []
    vector = []
    for i in range(n):
        if not stack:
            vector.append(i+1)
            stack.append(i)

        elif arr[stack[-1]] < arr[i]:
            vector.append(i-stack[-1])
            stack.append(i)

        else:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if not stack:
                vector.append(i+1)
                stack.append(i)
            else:
                vector.append(i-stack[-1])
                stack.append(i)
    vector1 = vector
    stack = []
    vector = []
    for i in range(n-1, -1, -1):
        if not stack:
            vector.append(n-i-1)
            stack.append(i)
        elif arr[stack[-1]] < arr[i]:
            vector.append(stack[-1]-i-1)
            stack.append(i)
        else:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if not stack:
                vector.append(n-i-1)
                stack.append(i)
            else:
                vector.append(stack[-1]-i-1)
                stack.append(i)

    vector = vector[::-1]
    for i in range(n):
        vector[i] += vector1[i]
        vector[i] *= arr[i]

    return max(vector)


arr = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 0, 0]]
row = len(arr)
col = len(arr[0])
h1 = arr[0]

maxi = maximum_area(h1,col)
for i in range(1,row):
    for j in range(0,col):
        if arr[i][j]==1:
            h1[j]+=1
        else:
            h1[j] = 0
    
    local = maximum_area(h1,col)
    maxi = max(maxi,local)

print(maxi)