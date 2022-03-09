arr = [4, 6, 8, 2, 12,6]
ans = []
k = 8


def printing(arr, local, ans, k, sumi, i):
    if sumi > k:
        return
    if i >= len(arr):
        if sumi == k:
            ans.append(local)
        return
    if len(ans)>1:
        return
    sumi += arr[i]
    printing(arr, local+[arr[i]], ans, k, sumi, i+1)
    sumi -= arr[i]
    printing(arr, local, ans, k, sumi, i+1)


printing(arr, [], ans, k, 0, 0)

print(ans)
