arr = [1,2,5,6,56,-10]
n =len(arr)-1
def sumi(arr,n):
    if n==0:
        return arr[0]

    return arr[n]+sumi(arr,n-1)

print(sum(arr))
print(sumi(arr,n))