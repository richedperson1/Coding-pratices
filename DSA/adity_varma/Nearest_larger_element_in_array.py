arr = [4,3,0,8,1,2,4]

i = len(arr)-1
stack = []
vector= []
while i>=0:
    if not stack:
        vector.append(-1)
        stack.append(arr[i])
    elif stack[-1]>arr[i]:
        vector.append(stack[-1])
        stack.append(arr[i])
    
    else:
        # j = len(stack)-1
        while len(stack)>0 and stack[-1] <= arr[i] :
            stack.pop()
        if len(stack)==0:
            vector.append(-1)
            stack.append(arr[i])
        else:
            vector.append(stack[-1])
            stack.append(arr[i])
    i-=1
print(vector[::-1])