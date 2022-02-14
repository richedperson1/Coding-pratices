arr = [1, -2, 30, 4, 8]

def solve(arr, ele):
    if len(arr) == 0 or arr[-1] >= ele:
        arr.append(ele)
        return

    num = arr[-1]
    arr.pop()
    solve(arr, ele)
    arr.append(num)


def sorted(arr):
    if len(arr) == 0:
        return
    num = arr[-1]
    arr.pop()
    sorted(arr)
    solve(arr, num)

sorted(arr)
print(arr)