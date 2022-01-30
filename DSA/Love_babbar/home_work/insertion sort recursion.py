arr = [8,7,6]
i = 1


def insertion(arr, i):
    if len(arr)==0 or len(arr)==1:
        return arr
    if i == len(arr):
        return arr

    j = i-1
    temp = arr[i]
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = temp
    # i += 1
    return insertion(arr, i+1)


print(insertion(arr, i))
