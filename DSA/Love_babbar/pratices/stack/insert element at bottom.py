def solve(arr,ele):
    if len(arr) ==0:
        arr.append(ele)
        return arr

    num = arr[-1]
    arr.pop()
    solve(arr,ele)
    arr.append(num)
    
arr = [1,2,3,4,5]
ele = 0
solve(arr,ele)
print(arr)