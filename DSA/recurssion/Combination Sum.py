arr = [2, 3, 5]
k = 10
arr = sorted(arr)
ans = []


def combine(arr, ans, local, i, k):
    if i >= len(arr):
        if k == 0:
            ans.append(local)
        return

    if k <= 0:
        if k == 0:
            ans.append(local)
        return

    combine(arr, ans, local+[arr[i]], i, k-arr[i])

    combine(arr, ans, local, i+1, k)


combine(arr, ans, [], 0, k)
print(ans)
