from collections import deque
q = deque()
arr = [-8, 2, 3, -6, 10]
k = 2
n = len(arr)
ans = []
for i in range(k):
    if arr[i]<0:
        q.append(i)

if len(q)>0:
    ans.append(arr[q[0]])

else:
    ans.append(0)

for i in range(k,n):
    if len(q)>0 and i-q[0]>=k:
        q.popleft()
    
    elif arr[i]<0:
        q.append(i)
    
    if len(q)>0:
        ans.append(arr[q[0]])
    else:
        ans.append(0)

print(ans)