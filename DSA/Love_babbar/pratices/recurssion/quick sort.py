arr = [3, 5, 8, 1, 6, 0, 2]

def partition(array,start,end):
        
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if(start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    return end

def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = partition(arr, low, high)

    quick_sort(arr, pivot+1, high)
    quick_sort(arr, low, pivot-1)

    return arr

high = len(arr)-1

print(quick_sort(arr, 0, high))
