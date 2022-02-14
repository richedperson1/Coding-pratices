arr = [1, 2, 3, 4, 5, 6, 7]


def solve(arr, ele):
    if len(arr) == 0:
        arr.append(ele)
        return

    num = arr[-1]
    arr.pop()

    solve(arr, ele)
    arr.append(num)



def reverse(arr):

    if len(arr) == 0:
        return arr

    n = arr[-1]
    arr.pop()

    reverse(arr)

    solve(arr, n)


reverse(arr)
print(arr)
