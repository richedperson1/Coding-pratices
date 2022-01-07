arr = [4,5,2,10,8]
# arr = [1,3,2,4]
stack = []
vector = []
n = len(arr)
for i in range(n-1,-1,-1):
    if not stack:
        vector.append(-1)
        stack.append(arr[i])
    
    elif stack[-1]<arr[i]:
        vector.append(stack[-1])
        stack.append(arr[i])
    
    else:
        while len(stack)>0 and stack[-1]>arr[i]:
            stack.pop()

        if len(stack)==0:
            vector.append(-1)
            stack.append(arr[i])

        else:
            vector.append(stack[-1])
            stack.append(arr[i])

        
print(vector[::-1])