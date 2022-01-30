arr = [56,89,41,63,6]
n = len(arr)


def selection_sort(arr, i):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if i == len(arr):
        return arr

    temp = i
    for j in range(i+1, n):
        if arr[temp] > arr[j]:
            temp = j

    local = arr[i]
    arr[i] = arr[temp]
    arr[temp] = local

    return selection_sort(arr, i+1)


print(selection_sort(arr, 0))
