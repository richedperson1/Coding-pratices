arr = [1,2,3,4,5]
n = len(arr)
k = (n//2)


def solve(arr, i,n):
    if i==(n//2):
        arr.pop()
        return

    a = arr[-1]
    arr.pop()
    solve(arr,i+1,n)
    arr.append(a)


solve(arr,0,n)
print(arr)