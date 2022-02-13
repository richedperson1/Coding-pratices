arr = [1,2,3,4,5,6]
n = len(arr)
high = n-1
low = 0
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def reversing(arr,i,j):
    if i>=j:
        return arr
    arr = swap(arr,i,j)
    return reversing(arr,i+1,j-1)

print(reversing(arr,low,high))