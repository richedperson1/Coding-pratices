arr = [1,2,1]
ans = []
k = 2


def printing(arr, local, ans, k, sumi, i):
    # if sumi > k:
    #     return 0

    if i >= len(arr):
        if sumi == k:
            return 1
        else:
            return 0

    sumi += arr[i]
    print(local,end='-->')
    l = printing(arr, local+[arr[i]], ans, k, sumi, i+1)
    sumi -= arr[i]
    r = printing(arr, local, ans, k, sumi, i+1)
    return l+r


print(printing(arr, [], ans, k, 0, 0))