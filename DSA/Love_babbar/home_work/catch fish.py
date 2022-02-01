"""
There is a pond with fish in it divided into ‘N’ segments. Each segment can contain at most 1 fish. You plan to go fishing, and want to catch ‘K’ fish in one attempt. To catch fish, you can drop a net of any size (not exceeding the size of the pond) on a continuous segment of a pond and catch all the fish present in that segment.

"""


def catch(arr, n, k):
    form = []
    total = 0
    for i in range(n):
        if arr[i]:
            form.append(i)
            total += 1

    if total < k:
        return -1

    ans = n
    j = 0
    for i in range(k-1, len(form)):
        ans = min(ans, form[i]-form[j]+1)
        j += 1

    return ans


arr = list(map(int, ('1 0 0 1 1').split()))
k = 3
n = len(arr)
print(catch(arr, n, k))
