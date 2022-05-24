arr = [1, 0, 3, 8, 2, 5]
brr = [1, 0, 3, 8, 2, 5]


def merge_arr(arr, ele):
    if len(arr) == 0 or arr[-1] < ele:
        arr.append(ele)
        return
    alpha = arr.pop()
    merge_arr(arr, ele)
    arr.append(alpha)


def sorting_arr(arr):
    if len(arr) == 1:
        return

    ele = arr.pop()
    sorting_arr(arr)
    merge_arr(arr, ele)


sorting_arr(arr)
print("The Un-Sorted array are : ")
print(brr)
print("The sorting array are : ")
print("Sorting by Recurrision : ", arr)
print("Sorting by inbuild fun : ", sorted(brr))
