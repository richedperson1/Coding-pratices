from queue import Queue
k = 2
q = Queue(maxsize=k)
arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(arr)
ans = []
for i in range(n):
    if q.full():
        flag = True
        while q.empty()==False:
            local = q[0]
            if local<0:
                ans.append(local)
                flag = False
                break
                
        if flag:
            ans.append(0)
    else:
        q.put(arr[i])

print(ans)
print()