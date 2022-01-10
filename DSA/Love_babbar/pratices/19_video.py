arr = list(map(int,("10 4 5 2 3 6 1 3 6").split()))
m = 3
def reverseArray(arr, m):
    # Write your code here.
    n = len(arr)
    j = n-1
    i = m+1
    while i<j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
  
    return arr

print(reverseArray(arr,m))