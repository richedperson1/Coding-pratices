arr = [1,8,6,9,0,-5,3]

n = len(arr)
j = 1

def bubble_sort(arr,n):
    if n==0 or n==1:
        return arr


    for j in range(n-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

    return bubble_sort(arr,n-1)

print(bubble_sort(arr,n))