arr = [10,12,59,2,36,0,87,3]
n  = len(arr)


ans = []

def divide_option(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_side = arr[:mid]
        right_side = arr[mid:]

        divide_option(left_side)

        divide_option(right_side)

        i = j = k = 0
        while i<len(left_side) and j< len(right_side):
            if left_side[i]<right_side[j]:
                arr[k] = left_side[i]
                i+=1
            else:
                arr[k] = right_side[j]
                j+=1
            k+=1

        while i < len(left_side):
            arr[k] = left_side[i]
            i+=1
            k+=1
        while j<len(right_side):
            arr[k] = right_side[j]
            j+=1
            k+=1

    return arr
print(sorted(arr))
print(divide_option(arr))
print(arr)