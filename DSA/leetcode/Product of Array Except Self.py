def product_arr(arr):
    n = len(arr)
    right = [0]*n
    total = 1
    for i in range(n):
        total*=arr[i]
        right[i] = total
        
    left = [0]*n
    total = 1
    for j in range(n-1,-1,-1):
        total *=arr[j]
        left[j] = total

    form =  [0]*n
    form[0] = left[1]
    form[-1] = right[-2] 

    for i in range(1,n-1):
        form[i] = left[i+1]*right[i-1]

    return form
arr = [1,2]
print(product_arr(arr))