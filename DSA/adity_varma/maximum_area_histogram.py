arr = [6, 2, 5, 4, 5, 1, 6]
n  = len(arr)

def stack_left(arr,n):
    stack =  []
    vector = []
    for i in range(n):
        if not stack:
            vector.append(i+1)
            stack.append(i)
        elif arr[stack[-1]]<arr[i]:
            vector.append(i-stack[-1])
            stack.append(i)
        else:
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            
            if not stack:
                vector.append(i+1)
                stack.append(i)
            else:
                vector.append(i-stack[-1])
                stack.append(i)
    return vector


def stack_right(arr,n):
    stack = []
    vector = []
    for i in range(n-1,-1,-1):
        if not stack:
            vector.append(n-i-1)
            stack.append(i)
        
        elif arr[stack[-1]]<arr[i]:
            vector.append(stack[-1]-i-1)
            stack.append(i)

        else:
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            
            if not stack:
                vector.append(n-i-1)
                stack.append(i)
            else:
                vector.append(stack[-1]-i-1)
                stack.append(i)
    return vector[::-1]
# print(arr)
left = stack_left(arr,n)
right = stack_right(arr,n)
total = []
for i in range(n):
    total.append((left[i]+right[i])*arr[i])

print(total)
