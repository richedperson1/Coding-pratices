arr = [2,3,1,2,3,4,5,6]

peak = False
vell = False

n = len(arr)
res = 0
i = 1
while i<n:
    if arr[i-1]<arr[i]:
        start = i
        while i<n and arr[i-1]<arr[i]:
            peak = True
            i+=1
        while i<n and arr[i-1]>arr[i]:
            vell = True
            i+=1

        if peak and vell:
            res = max(res,i-start+1)

        peak = False
        vell = False
    else:
        i+=1

print(res)
            
