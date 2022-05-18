import sys
import copy

arr = [2, 1, 3, 4, 5, 6, 7, 8]


def reverse(arr, i, j):
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
        reverse(arr, i+1, j-1)

    return arr


print(reverse(arr, 0, len(arr)-1))  # In this we give array by referance only
print(arr)

# ------------------------------------------------------------------------------------------------ #
array = [2, 1, 3, 4, 5, 6, 7, 8]
arr = copy.copy(array)


def reverse_copy(arr, i, j):
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
        reverse(arr, i+1, j-1)

    return arr


print(reverse_copy(array, 0, len(array)-1))
print("The referance count of array is : ", sys.getrefcount(array))
